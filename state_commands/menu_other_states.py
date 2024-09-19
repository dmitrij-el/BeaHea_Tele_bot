"""
Сборник реакций на сообщения пользователя в состояниях относящихся к главному меню и другим несортированным состояниям
"""
import asyncio

from aiogram import Router
from aiogram import flags
from aiogram.types import Message, PreCheckoutQuery
from aiogram.fsm.context import FSMContext

from config.config import TEST_PAYMENT_TOKEN_SBERBANK
from data.models_peewee import User
from data import text, text_user_profile, text_of_paid_service, price
from keyboards import kb_user_profile, kb_user_questions, kb_main_menu
from states.states import StateMenu

router = Router()


async def delete_msgs(msg, dlt_msg):
    await asyncio.sleep(5)
    await dlt_msg.delete()
    await asyncio.sleep(5)
    await msg.delete()


@router.message(StateMenu.menu)
@flags.chat_action("typing")
async def main_menu(msg: Message, state: FSMContext):
    """Главное меню"""
    prompt = msg.text
    if prompt == 'Телеграм-канал':
        await msg.answer(text=text.go_to_telegram_channel, reply_markup=kb_main_menu.go_to_telegram_channel())
        await state.set_state(StateMenu.menu)
    elif prompt == '👤 Профиль':
        await msg.answer(text=text.go_to_point_menu,
                         reply_markup=kb_user_profile.user_profile())
        await state.set_state(StateMenu.profile)
    elif prompt == 'Марафон':
        if User.subscribe_marathon:
            await msg.answer(text=text_of_paid_service.subscribe_marathon_not_paid_for,
                             reply_markup=kb_main_menu.go_to_telegram_channel())
        else:
            await msg.answer(text=text_of_paid_service.subscribe_marathon_paid_for,
                             reply_markup=kb_main_menu.go_to_telegram_channel())
        await state.set_state(StateMenu.menu)
    elif prompt == 'Частный канал':
        if User.subscribe_on_private_channel:
            await msg.answer(text=text.go_to_telegram_channel, reply_markup=kb_main_menu.go_to_telegram_channel())
            await state.set_state(StateMenu.menu)

        else:
            await msg.answer(text=text_of_paid_service.subscribe_private_channel_paid_for,
                             reply_markup=kb_main_menu.go_to_telegram_channel())
            await state.set_state(StateMenu.menu)


@router.message(StateMenu.buy_subscription)
@flags.chat_action("typing")
async def private_channel(msg: Message, state: FSMContext):
    if TEST_PAYMENT_TOKEN_SBERBANK.split(':')[1] == 'TEST':
        await msg.answer("!!!Тестовый платеж!!!")
        await msg.answer_invoice(title="Подписка на бота",
                                 description="Активация подписки на бота на 1 месяц",
                                 provider_token=TEST_PAYMENT_TOKEN_SBERBANK,
                                 lable='RUB',
                                 currency="rub",
                                 photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium"
                                           "-subscription.jpg",
                                 photo_width=416,
                                 photo_height=234,
                                 photo_size=416,
                                 is_flexible=False,
                                 prices=[price.PRICE_SUBSCRIPTION],
                                 start_parameter="one-month-subscription", payload="test-invoice-payload")


@router.message(lambda query: True)
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


@router.message()
async def successful_payment_subscribe(msg: Message):
    await msg.answer(text="🥳Спасибо за вашу поддержку!🤗")


@router.message(StateMenu.profile)
@flags.chat_action("typing")
async def marathon_channel(msg: Message, state: FSMContext):
    pass


@router.message(StateMenu.profile)
@flags.chat_action("typing")
async def profile(msg: Message, state: FSMContext):
    """Меню аккаунта"""
    prompt = msg.text
    commands = text_user_profile.question_for_profile
    for command in commands.values():
        if prompt == command[0] and prompt != text_user_profile.question_for_profile['the_basic_data'][0]:
            await state.set_state(command[2])
            dlt_msg = await msg.answer(text=command[1],
                                       reply_markup=kb_user_questions.user_redactor_question_for_profile(
                                           user_id=msg.from_user.id))
            break
        elif prompt == text_user_profile.question_for_profile['the_basic_data'][0]:

            await state.set_state(command[2])
            dlt_msg = await msg.answer(text=command[1],
                                       reply_markup=kb_user_profile.user_profile_basic_data(user_id=msg.from_user.id))
            break
    else:
        await state.set_state(StateMenu.profile)
        dlt_msg = await msg.answer(text=text.err_command,
                                   reply_markup=kb_user_profile.user_profile())

import datetime

from aiogram import Bot
from aiogram import F, Router
from aiogram.types import (CallbackQuery,
                           Message,
                           PreCheckoutQuery,
                           ContentType,
                           ShippingQuery,
                           LabeledPrice,
                           successful_payment)
from aiogram.fsm.context import FSMContext

import states.states
from config.config import TEST_PAYMENT_TOKEN_YOU_KASSA, TEST_PAYMENT_TOKEN_SBERBANK
from datas import models, price
from datas.models.models_setting import User
from states.states import StateMenu
from keyboards import kb_main_menu, kb_pay_menu

router = Router()


@router.callback_query(F.data == 'pay_subscription')
async def go_to_private_telegram_channel(clbck: CallbackQuery) -> None:
    await clbck.bot.send_invoice(
        chat_id=clbck.from_user.id,
        title='Подписка на закрытый канал',
        description='Всякое разное о сути канала и т.д.',
        provider_token=TEST_PAYMENT_TOKEN_SBERBANK,
        currency='rub',
        photo_url='https://www.emkosti-online.ru/upload/medialibrary/9be'
                  '/9be2c8e675ef806772b418183bf4aae2.png',
        photo_height=512,  # !=0/None, иначе изображение не покажется
        photo_width=512,
        photo_size=512,
        is_flexible=False,  # True если конечная цена зависит от способа доставки
        prices=[price.PRICE_SUBSCRIPTION],
        start_parameter='subscription',
        payload='subscription'
    )


@router.callback_query(F.data == 'pay_marathon')
async def go_to_private_telegram_channel(clbck: CallbackQuery) -> None:
    await clbck.bot.send_invoice(
        chat_id=clbck.from_user.id,
        title='Подписка на марафон мечты',
        description='Всякое разное о марафоне и т.д.',
        provider_token=TEST_PAYMENT_TOKEN_SBERBANK,
        currency='rub',
        photo_url='https://www.emkosti-online.ru/upload/medialibrary/9be'
                  '/9be2c8e675ef806772b418183bf4aae2.png',
        photo_height=512,  # !=0/None, иначе изображение не покажется
        photo_width=512,
        photo_size=512,
        is_flexible=False,  # True если конечная цена зависит от способа доставки
        prices=[price.PRICE_MARATHON],
        start_parameter='marathon',
        payload='marathon'
    )


@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery,
                                     bot: Bot) -> None:
    await bot.answer_pre_checkout_query(pre_checkout_query.id,
                                        ok=True)


async def process_successful_payment(msg: Message) -> None:
    i = msg.successful_payment
    if i.invoice_payload == 'subscription':
        user = (User.update(subscribe_on_private_channel=1,
                            date_subscribe_on_private_channel=datetime.datetime.now(),
                            date_end_subscribe_on_private_channel=datetime.datetime.now()
                                                                  + datetime.timedelta(days=28)).
                where(User.user_id == msg.from_user.id))
        user.execute()
        await msg.answer(text='Оплата подписки на частный канал прошла успешно',
                         reply_markup=kb_pay_menu.go_to_private_telegram_channel())
    elif i.invoice_payload == 'marathon':
        user = (User.update(subscribe_marathon=1,
                            date_subscribe_marathon=datetime.datetime.now(),
                            date_end_subscribe_marathon=datetime.datetime.now()
                                                        + datetime.timedelta(days=28)).
                where(User.user_id == msg.from_user.id))
        user.execute()
        await msg.answer(text='Оплата подписки на марафон прошла успешно',
                         reply_markup=kb_pay_menu.go_to_marathon_channel())

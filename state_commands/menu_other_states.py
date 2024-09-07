"""
Сборник реакций на сообщения пользователя в состояниях относящихся к главному меню и другим несортированным состояниям
"""
import asyncio

from aiogram import Router
from aiogram import flags
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data import text, text_user_profile, db_funcs_user_account
from keyboards import kb_user_profile, kb_user_questions
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
        await msg.answer(text=text.go_to_telegram_channel, reply_markup=kb_user_profile.go_to_telegram_channel())
        await state.set_state(StateMenu.menu)
    elif prompt == '👤 Профиль':
        await msg.answer(text=text.go_to_point_menu,
                         reply_markup=kb_user_profile.user_profile())
        await state.set_state(StateMenu.profile)
    elif prompt == 'Марафон':
        await msg.answer(text=text.go_to_telegram_channel, reply_markup=kb_user_profile.go_to_telegram_channel())
        await state.set_state(StateMenu.menu)
    elif prompt == 'Частный канал':
        await msg.answer(text=text.go_to_telegram_channel, reply_markup=kb_user_profile.go_to_telegram_channel())
        await state.set_state(StateMenu.menu)

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
                                   reply_markup=kb_user_profile.user_profile(user_id=msg.from_user.id))

"""
Сборник реакций на сообщения пользователя в состояниях относящихся к главному меню и другим несортированным состояниям
"""
from aiogram import Router
from aiogram import flags
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from data import text
from keyboards import kb_user_profile
from states.states import StateMenu

router = Router()


@router.message(StateMenu.menu)
@flags.chat_action("typing")
async def main_menu(msg: Message, state: FSMContext):
    """Главное меню"""
    prompt = msg.text
    if prompt == 'Телеграм-канал':
        await msg.delete()
        await msg.answer(text=text.go_to_telegram_channel, reply_markup=kb_user_profile.go_to_telegram_channel())
        await state.set_state(StateMenu.menu)
    elif prompt == '👤 Профиль':
        await msg.delete()
        await msg.answer(text=text.go_to_point_menu, reply_markup=kb_user_profile.user_profile(user_id=msg.from_user.id))
        await state.set_state(StateMenu.profile)

"""
Сборник реакций на сообщения пользователя в состояниях относящихся к главному меню и другим несортированным состояниям
"""
from aiogram import Router
from aiogram import flags
from aiogram.types import Message

from data import text
from keyboards import kb_user_profile
from states.states import StateGen, StateMenu

router = Router()


@router.message(StateGen.menu)
@flags.chat_action("typing")
async def main_menu(msg: Message):
    """Главное меню"""
    prompt = msg.text
    await msg.answer(text=text.menu, reply_markup=kb_user_profile.main_menu())
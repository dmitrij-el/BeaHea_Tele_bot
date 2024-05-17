"""
Сборник реакций на сообщения пользователя в состояниях относящихся к главному меню и другим несортированным состояниям
"""
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import flags

from Tbot_beahea.states.states import StateGen
from Tbot_beahea.keyboards import kb
from Tbot_beahea.data import text


router = Router()


@router.message(StateGen.menu)
@flags.chat_action("typing")
async def main_menu(msg: Message, state: FSMContext):
    """Главное меню"""
    await msg.answer(text=text.menu, reply_markup=kb.main_menu())



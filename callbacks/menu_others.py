"""
Здесь хранятся колбэки, которые реагируют на вызовы из telebot/keyboards/kb.py
и вводят состояние, которое определяет поведение бота.
Также каждый колбэк после вызова сразу выполняет заложенный в него функционал,
до получения сообщения от пользователя.


"""


from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from Tbot_beahea.keyboards import kb
from Tbot_beahea.data import text, db_funcs
from Tbot_beahea.utils import easy_funcs

from Tbot_beahea.states.states import (StateGen,
                                       StateMenu,
                                       StateUserProfile)



router = Router()



@router.callback_query(F.data == "menu")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    """
    Колбэк Главного меню.
    """
    await state.set_state(StateGen.menu)
    await clbck.message.answer(text.menu, reply_markup=kb.main_menu())



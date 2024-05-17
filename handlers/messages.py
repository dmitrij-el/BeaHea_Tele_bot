from aiogram import F, Router
from aiogram.types import Message

from Tbot_beahea.keyboards import kb
from Tbot_beahea.data import db_funcs, text

router = Router()



@router.message(F.text == "Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.main_menu())



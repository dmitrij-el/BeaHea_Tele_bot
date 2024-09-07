from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.states import StateMenu
from data import text
from keyboards import kb_user_profile


router = Router()


@router.message(F.text.lower().in_({"выйти в меню", "главное меню"}))
async def menu(msg: Message, state: FSMContext):
    await msg.delete()
    await state.set_state(StateMenu.menu)
    await msg.answer(text=text.go_to_point_menu,
                     reply_markup=kb_user_profile.main_menu())

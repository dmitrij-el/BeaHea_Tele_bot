from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.states import StateGen
from data import text, db_funcs_user_account
from keyboards import kb_user_profile


router = Router()


@router.message(F.text.lower().in_({"выйти в меню", "главное меню"}))
async def menu(msg: Message, state: FSMContext):
    await msg.answer(text=text.close_all_keyboards, reply_markup=kb_user_profile.ReplyKeyboardRemove())
    await msg.answer(text.menu, reply_markup=kb_user_profile.main_menu())
    await state.set_state(StateGen.menu)




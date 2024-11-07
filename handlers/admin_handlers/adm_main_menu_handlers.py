from aiogram import Router, flags
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from datas.models.models_user import AdminList
from datas.texts import text_admin_navigator
from states.states import StateAdminMenu
from keyboards.kb_admin import kb_admin_menu
from handlers.required import admin_required


router = Router()


@router.message(Command('admin_main_menu'))
@router.message(StateAdminMenu.admin_main_menu)
@admin_required
@flags.chat_action("typing")
async def admin_main_menu(msg: Message, state: FSMContext) -> None:
    await state.set_state(StateAdminMenu.admin_main_menu)
    user_id = msg.from_user.id
    prompt = msg.text
    if prompt == "Администраторы":
        answer = await AdminList.load_admin_list()
        for ans in answer:
            await msg.answer(text=ans)
        await msg.answer(text=text_admin_navigator.admin_admin_list,
                         reply_markup=kb_admin_menu.admin_add_del_back(user_id=user_id))
        await state.set_state(StateAdminMenu.admin_admin_list)

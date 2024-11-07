from functools import wraps

from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config.config import ADMIN_DIMA
from datas.models.models_user import Admin, User
from datas.texts import text_admin_navigator, text
from states.states import StateMenu
from keyboards import kb_main_menu


async def set_previous_state(state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.update_data(previous_state=current_state)


def admin_required(func):
    @wraps(func)
    async def wrapper(msg: Message, state: FSMContext,  *args, **kwargs):
        await set_previous_state(state)
        if Admin.is_admin(msg.from_user.id):
            await func(msg, state, *args, **kwargs)
        else:
            await msg.answer(text=text_admin_navigator.err_admin_access_rights,
                             reply_markup=kb_main_menu.main_menu(user_id=msg.from_user.id))
            await state.set_state(StateMenu.main_menu)

    return wrapper


def user_required(func):
    @wraps(func)
    async def wrapper(msg: Message, state: FSMContext, bot: Bot,  *args, **kwargs):
        await set_previous_state(state)
        user = User.get_user_by_id(msg.from_user.id)
        if user:
            await func(msg, state, bot, *args, **kwargs)
        else:
            prompt = msg.text
            await msg.answer(text=text.err_user_access_rights)
            await msg.answer(text=text.err_reg_fatal)
            await bot.send_message(chat_id=int(ADMIN_DIMA), text=prompt)

    return wrapper
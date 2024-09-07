
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards import kb_user_profile
from data import db_funcs_user_account, text
from states.states import StateMenu, StateUserProfile

router = Router()


@router.message(Command('start'))
async def handler_start(msg: Message, state: FSMContext):
    """
    Реагирует на команду 'start'. При вызове проверяет на наличие юзера.
    Если юзера нет записывает данные пользователя в БД.
    Если есть, предлагает обнулить данные.


    :param msg: Сообщение от пользователя
    :param state: Состояние бота

    """

    user_id = msg.from_user.id
    user = db_funcs_user_account.check_user_datas(user_id=user_id)
    if user:
        await msg.answer(text=text.greet_cont.format(user_id=user_id), reply_markup=kb_user_profile.main_menu())
        await state.set_state(StateMenu.menu)

    else:
        acc_dict = {
            'user_id': msg.from_user.id,
            'name': msg.from_user.first_name,
            'surname': msg.from_user.last_name,
            'username': msg.from_user.username
        }
        db_funcs_user_account.user_rec_datas_in_reg(user_id=user_id, acc_dict = acc_dict)
        if db_funcs_user_account.check_user_datas(user_id):
            await msg.answer(text=text.greet_cont.format(user_id=user_id), reply_markup=kb_user_profile.main_menu())
        else:
            await msg.answer(text=text.err_reg_fatal)
            prompt = msg.text
            await msg.answer(text=prompt, reply_markup=kb_user_profile.main_menu())
    await state.set_state(StateMenu.menu)


@router.message(Command('menu'))
async def handler_main_menu(msg: Message, state: FSMContext):
    """
    Реагирует на команду 'main_menu'. При вызове отправляет в главное меня.

    :param msg: Сообщение от пользователя
    :param state: Состояние бота
    """
    await msg.answer(text=text.menu, reply_markup=kb_user_profile.main_menu())
    await msg.delete()
    await state.set_state(StateMenu.menu)


@router.message(Command('help'))
async def handler_send_help(msg: Message, state: FSMContext):
    """
    Отправляет список команд для использования.

    :param msg: Сообщение от пользователя
    """
    await state.set_state(StateMenu.menu)
    await msg.answer(text="Вот список команд для использования")
    await msg.answer(text="""
/start - Запуск бота. Автоматически создается аккаунт. При повторном вызове предлагает сбросить профиль.
/main_menu - Выводит главное меню.
/help - Список команд
""",
                     reply_markup=kb_user_profile.main_menu())

"""
Сборник реакций на сообщения пользователя в состояниях относящихся к аккаунту
"""
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import flags

from Tbot_beahea.states.states import (StateMenu, StateUserProfile)
from Tbot_beahea.utils import easy_funcs
from Tbot_beahea.keyboards import kb
from Tbot_beahea.data import db_funcs, text
from Tbot_beahea.data.db_funcs import change_datas

router = Router()




@router.message(StateMenu.profile)
@flags.chat_action("typing")
async def generate_text(msg: Message, state: FSMContext):
    """Меню аккаунта"""
    await msg.answer()


@router.message(StateUserProfile.clear_profile)
async def clear_profile(msg: Message, state: FSMContext):
    """Очистка аккаунта"""
    prompt = msg.text
    if prompt == "Да":
        mesg = await msg.answer(text.clear_account_wait)
        db_funcs.user_delete_datas(msg.from_user.id)
        if db_funcs.check_user_datas(msg.from_user.id):
            acc_dict = {
                'user_id': msg.from_user.id,
                'name': msg.from_user.first_name,
                'surname': msg.from_user.last_name,
                'username': msg.from_user.username
            }
            db_funcs.user_rec_datas_in_reg(acc_dict)
            await mesg.answer(text=text.clear_account_true, reply_markup=kb.ReplyKeyboardRemove())
        else:
            await mesg.answer(text=text.err, reply_markup=kb.ReplyKeyboardRemove())
        await mesg.answer(text=text.menu, reply_markup=kb.clear_profile_menu())
    elif prompt == "Нет":
        await msg.answer(text=text.clear_account_cancel, reply_markup=kb.ReplyKeyboardRemove())
        await msg.answer(text=text.menu, reply_markup=kb.clear_profile_menu())


@router.message(StateUserProfile.change_name)
@flags.chat_action("typing")
async def change_name(msg: Message, state: FSMContext):
    """Изменение имени"""
    await change_datas(msg, change_data='user_name')


@router.message(StateUserProfile.change_surname)
@flags.chat_action("typing")
async def change_surname(msg: Message, state: FSMContext):
    """Изменение фамилии"""
    await change_datas(msg, change_data='user_surname')

@router.message(StateUserProfile.change_patronymic)
@flags.chat_action("typing")
async def change_surname(msg: Message, state: FSMContext):
    """Изменение отчества"""
    await change_datas(msg, change_data='user_patronymic')


@router.message(StateUserProfile.change_date_birth)
@flags.chat_action("typing")
async def change_date_birth(msg: Message, state: FSMContext):
    """Изменение даты рождения"""
    await change_datas(msg=msg, change_data='date_birth')


@router.message(StateUserProfile.change_gender)
@flags.chat_action("typing")
async def change_gender(msg: Message, state: FSMContext):
    """Изменение пола"""
    await change_datas(msg=msg, change_data='gender')


@router.message(StateUserProfile.change_height)
@flags.chat_action("typing")
async def change_gender(msg: Message, state: FSMContext):
    """Изменение роста"""
    await change_datas(msg=msg, change_data='height')


@router.message(StateUserProfile.change_weight)
@flags.chat_action("typing")
async def change_gender(msg: Message, state: FSMContext):
    """Изменение веса"""
    await change_datas(msg=msg, change_data='weight')


@router.message(StateUserProfile.change_email)
@flags.chat_action("typing")
async def change_gender(msg: Message, state: FSMContext):
    """Изменение адреса почты"""
    await change_datas(msg=msg, change_data='email')


@router.message(StateUserProfile.change_phone)
@flags.chat_action("typing")
async def change_gender(msg: Message, state: FSMContext):
    """Изменение номера телефона"""
    await change_datas(msg=msg, change_data='phone')

@router.message(StateUserProfile.change_communication_channels)
@flags.chat_action("typing")
async def change_gender(msg: Message, state: FSMContext):
    """Изменение канала связи"""
    await change_datas(msg=msg, change_data='communication_channels')
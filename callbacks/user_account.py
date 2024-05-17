"""
Здесь хранятся колбэки, которые реагируют на вызовы из telebot/keyboards/kb.py
и вводят состояние, которое определяет поведение бота.
Также каждый колбэк после вызова сразу выполняет заложенный в него функционал,
до получения сообщения от пользователя.


"""
from typing import Coroutine

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from Tbot_beahea.keyboards import kb
from Tbot_beahea.data import text, db_funcs
from Tbot_beahea.utils import easy_funcs

from Tbot_beahea.states.states import (StateGen,
                                       StateMenu,
                                       StateUserProfile)


router = Router()



@router.callback_query(F.data == "creat_error_profile")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    """
    Колбэк Регистрации аккаунта в случае ошибки.
    """
    acc_dict = {
        'user_id': clbck.from_user.id,
        'name': clbck.from_user.first_name,
        'surname': clbck.from_user.last_name,
        'username': clbck.from_user.username
    }
    db_funcs.user_rec_datas_in_reg(acc_dict)

    await clbck.message.answer(text.account_menu, reply_markup=kb.user_profile(user_id=clbck.from_user.id))
    await state.set_state(StateUserProfile)



@router.callback_query(F.data == "user_profile")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(StateMenu.profile)
    await clbck.message.answer(text.account_menu, reply_markup=kb.user_profile(clbck.from_user.id))

@router.callback_query(F.data == "clear_profile")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text.clear_account_question, reply_markup=kb.choiceYN(text.clear_account_question))
    await state.set_state(StateUserProfile.clear_profile)


@router.callback_query(F.data == "change_name")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_name)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(text=text.profile_name.format(user_name=user.name))
    await clbck.message.answer(text.update_profile_enter_data,
                               reply_markup=kb.back_button(text.update_profile_enter_data))


@router.callback_query(F.data == "change_surname")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_surname)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(text=text.profile_surname.format(user_surname=user.surname))
    await clbck.message.answer(text.update_profile_enter_data,
                               reply_markup=kb.back_button(text.update_profile_enter_data))


@router.callback_query(F.data == "change_patronymic")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_patronymic)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(text=text.profile_patronymic.format(user_patronymic=user.patronymic))
    await clbck.message.answer(text.update_profile_enter_data,
                               reply_markup=kb.back_button(text.update_profile_enter_data))


@router.callback_query(F.data == "change_date_birth")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_date_birth)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(text=text.profile_date_birth.format(date_birth=user.date_birth))
    await clbck.message.answer(text.update_profile_enter_data,
                               reply_markup=kb.back_button(text.update_profile_enter_data))


@router.callback_query(F.data == "change_gender")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_gender)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(text=text.profile_gender.format(gender=user.gender))
    await clbck.message.answer(text.update_profile_enter_data,
                               reply_markup=kb.back_button(text.update_profile_enter_data))


@router.callback_query(F.data == "change_height")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_gender)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(text=text.profile_height.format(height=user.height))
    await clbck.message.answer(text.update_profile_enter_data,
                               reply_markup=kb.back_button(text.update_profile_enter_data))


@router.callback_query(F.data == "change_weight")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_weight)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(text=text.profile_weight.format(weight=user.weight))
    await clbck.message.answer(text.update_profile_enter_data,
                               reply_markup=kb.back_button(text.update_profile_enter_data))


@router.callback_query(F.data == "change_email")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_email)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(text=text.profile_email.format(email=user.email))
    await clbck.message.answer(text.update_email, reply_markup=kb.back_button(text.update_profile_enter_data))


@router.callback_query(F.data == "change_phone")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_phone)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(text=text.profile_phone.format(phone=user.phone))
    await clbck.message.answer(text.update_phone, reply_markup=kb.back_button(text.update_profile_enter_data))


@router.callback_query(F.data == "change_communication_channels")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext) -> Coroutine:
    await state.set_state(StateUserProfile.change_communication_channels)
    user = db_funcs.user_get_data(user_id=clbck.from_user.id)
    await clbck.message.answer(
        text=text.profile_communication_channels.format(communication_channels=user.communication_channels))
    await clbck.message.answer(text.update_communication_channels,
                               reply_markup=kb.back_button(text.update_profile_enter_data))

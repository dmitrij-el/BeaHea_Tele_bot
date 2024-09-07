"""
Сборник реакций на сообщения пользователя в состояниях относящихся к аккаунту
"""
import asyncio

from aiogram import Router
from aiogram import flags
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data import db_funcs_user_account, text, text_user_profile
from data.models_peewee import User, Gender, ChannelCom, UserProfileBasicData
from keyboards import kb_user_profile
from states.states import (StateMenu,
                           StateUserProfile,
                           StateUserProfileBasicData,
                           StateUserProfileQuestionnaire,
                           StateUserProfileGoals,
                           StateUserProfileTrain)
from state_commands.menu_other_states import delete_msgs
from utils import easy_funcs

router = Router()


def find_column_name_by_value(model_instance, search_value):
    """
    Функция для поиска имени столбца по значению в конкретной записи модели Peewee.
    :param model_instance: Экземпляр модели Peewee (одна запись).
    :param search_value: Значение для поиска.
    :return: Имя столбца или None, если значение не найдено.
    """
    for field in model_instance._meta.sorted_fields:
        field_value = getattr(model_instance, field.name)
        if field_value == search_value:
            return field.name
    return None


@router.message(StateUserProfile.the_basic_data)
async def clear_profile(msg: Message, state: FSMContext):

    prompt = msg.text
    user_id = msg.from_user.id
    the_basic_data = UserProfileBasicData.select().where(UserProfileBasicData.user_id == user_id).get()
    res = find_column_name_by_value(the_basic_data, prompt)
    if res in text_user_profile.account_basic_data['basic_data'].keys():
        await state.set_state(state=text_user_profile.account_basic_data['basic_data'][res][1])
        await msg.answer(text=text_user_profile.account_basic_data['basic_data'][res][2])
    elif prompt == 'Назад':
        await state.set_state(state=StateMenu.profile)
        await msg.answer(text=text_user_profile.question_for_profile['the_basic_data'][1],
                         reply_markup=kb_user_profile.user_profile())
    elif prompt == 'Главное меню':
        await state.set_state(state=StateMenu.menu)
        await msg.answer(text=text.menu,
                         reply_markup=kb_user_profile.main_menu())
    for val in text_user_profile.account_basic_data['basic_data'].values():
        if val[0] == prompt:
            await state.set_state(state=val[1])


@router.message(StateUserProfileBasicData.clear_profile)
async def clear_profile(msg: Message, state: FSMContext):
    """Очистка аккаунта"""
    prompt = msg.text
    if prompt == "Да":
        mess = await msg.answer(text.clear_account_wait)

        delete_acc = db_funcs_user_account.user_delete_datas(msg.from_user.id)
        if delete_acc:
            acc_dict = {
                'user_id': msg.from_user.id,
                'name': msg.from_user.first_name,
                'surname': msg.from_user.last_name,
                'username': msg.from_user.username
            }
            db_funcs_user_account.user_rec_datas_in_reg(acc_dict)
            await mess.answer(text=text.clear_account_true, reply_markup=kb_user_profile.ReplyKeyboardRemove())
        else:
            await mess.answer(text=text.err, reply_markup=kb_user_profile.ReplyKeyboardRemove())
        await mess.answer(text=text.menu, reply_markup=kb_user_profile.main_menu())
    elif prompt == "Нет":
        await msg.answer(text=text.clear_account_cancel, reply_markup=kb_user_profile.ReplyKeyboardRemove())
        await msg.answer(text=text.menu, reply_markup=kb_user_profile.main_menu())


@router.message(StateUserProfileBasicData.name,
                StateUserProfileBasicData.surname,
                StateUserProfileBasicData.patronymic,
                StateUserProfileBasicData.date_birth,
                StateUserProfileBasicData.height,
                StateUserProfileBasicData.weight,
                StateUserProfileBasicData.email)
@flags.chat_action("typing")
async def change_name(msg: Message, state: FSMContext):
    """Изменение имени"""
    prompt = msg.text
    if prompt == 'Назад':
        await state.set_state(state=StateUserProfile.the_basic_data)
        await msg.answer(text=text_user_profile.account_basic_data,
                         reply_markup=kb_user_profile.user_profile_basic_data(user_id=msg.from_user.id))
    elif prompt == 'Главное меню':
        await state.set_state(state=StateMenu.menu)
        await msg.answer(text=text.menu,
                         reply_markup=kb_user_profile.main_menu())
    else:
        for key, value in text_user_profile.account_basic_data['basic_data_states'].items():
            if value == state.get_state():
                (UserProfileBasicData.update({key: prompt}).
                 where(UserProfileBasicData.user_id==msg.from_user.id))
      ############
        ##########
    ###########
    ###########

@router.message(StateUserProfileBasicData.gender)
@flags.chat_action("typing")
async def change_gender(msg: Message):
    """Изменение пола"""
    prompt = msg.text
    if prompt == 'Отмена':
        await msg.answer(text.update_account_cancel, reply_markup=kb_user_profile.ReplyKeyboardRemove())
        await msg.answer(text=text.account_menu_2,
                         reply_markup=kb_user_profile.user_profile())
    else:
        mess = await msg.answer(text.update_profile_wait)
        user = User.select().where(User.user_id == msg.from_user.id).get()
        genders = Gender.select()
        for data in [(gender.name, gender.symbol) for gender in genders]:
            if prompt in data:
                user.gender = Gender.select(Gender.id).where(Gender.name == data[0]).get()
                user.save()
                await mess.answer(text=text.update_account_true, reply_markup=kb_user_profile.ReplyKeyboardRemove())
                break
        else:
            await mess.answer(text=text_user_profile.account_basic_data['err_basic_data_update']['gender'],
                              reply_markup=kb_user_profile.ReplyKeyboardRemove())
        await msg.answer(text.account_menu_2, reply_markup=kb_user_profile.user_profile())


@router.message(StateUserProfileBasicData.phone)
@flags.chat_action("typing")
async def change_phone(msg: Message):
    """Изменение номера телефона"""
    prompt = msg.text
    contact = msg.contact
    print(contact)
    if prompt:
        pass
    elif contact:
        pass
    else:
        await msg.answer(text=text.err, reply_markup=kb_user_profile.ReplyKeyboardRemove())
        await msg.answer(text=text.account_menu_2, reply_markup=kb_user_profile.user_profile(msg.from_user.id))


@router.message(StateUserProfileBasicData.communication_channels)
@flags.chat_action("typing")
async def change_channel(msg: Message):
    """Изменение канала связи"""
    prompt = msg.text
    if prompt == 'Отмена':
        await msg.answer(text.update_account_cancel, reply_markup=kb_user_profile.ReplyKeyboardRemove())
        await msg.answer(text=text.account_menu_2,
                         reply_markup=kb_user_profile.user_profile())
    else:
        mess = await msg.answer(text.update_profile_wait)
        user = User.select().where(User.user_id == msg.from_user.id).get()
        channels = ChannelCom.select()
        for data in [channel.name for channel in channels]:
            if prompt in data:
                user.communication_channels = ChannelCom.select(ChannelCom.id).where(ChannelCom.name == prompt).get()
                user.save()
                await msg.answer(text=text.update_account_true, reply_markup=kb_user_profile.ReplyKeyboardRemove())
                break
        else:
            await mess.answer(text=text_user_profile.account_basic_data['err_basic_data_update']['gender'],
                              reply_markup=kb_user_profile.ReplyKeyboardRemove())
        await msg.answer(text.account_menu_2, reply_markup=kb_user_profile.user_profile())

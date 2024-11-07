"""
Сборник реакций на сообщения пользователя в состояниях относящихся к аккаунту
"""
import json

from aiogram import Router, Bot
from aiogram import flags
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Filter

from handlers.required import user_required
from datas.texts import text, text_account_basic_datas, text_user_questions
from datas.models.models_setting import User, Gender, UserBasicData
from keyboards import kb_main_menu
from keyboards.kb_user import kb_user_profile, kb_the_basic_data, kb_the_questionnaire, kb_the_body_parameters
from states.states import (StateMenu,
                           StateUserProfile,
                           StateUserProfileBasicData)
from utils import easy_funcs

router = Router()


class ProfileStateFilter(Filter):
    async def __call__(self, message: Message, state: FSMContext) -> bool:
        current_state = await state.get_state()
        return current_state in [
            StateUserProfileBasicData.name,
            StateUserProfileBasicData.surname,
            StateUserProfileBasicData.patronymic,
            StateUserProfileBasicData.date_birth,
            StateUserProfileBasicData.email
        ]

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
@user_required
@flags.chat_action("typing")
async def the_basic_data(msg: Message, state: FSMContext, bot: Bot):
    prompt =msg.text
    user_id = msg.from_user.id
    if prompt.lower() == "назад":
        await msg.answer(text=text_account_basic_datas.account_menu,
                         reply_markup=kb_user_profile.user_profile())
        await state.set_state(StateMenu.user_profile)
    else:
        # Получаем данные пользователя, перебирая заменяем нулевые значения на стандартные,
        # потом сравниваем с промнтом
        basic_data = UserBasicData.get_as_dict(user_id=user_id)

        # Выводим данные
        print(basic_data)
        return
        for key, value in the_basic_data:
            print(key)
            if value is None:
                value = text_account_basic_datas.basic_data_menu[key]
            if prompt == value:
                next_state = getattr(StateUserProfileBasicData, key)
                text_mess = text_account_basic_datas.basic_data_update[key]
                if key == 'gender':
                    kb = kb_the_basic_data.gender()
                elif key == 'communication_channels':
                    kb = kb_the_basic_data.communication_channels()
                else:
                    kb = kb_user_profile.back_button()
                break

        else:
            text_mess=text.err_command
            kb=kb_user_profile.the_basic_data(user_id=user_id)
            next_state = StateUserProfile.the_basic_data
        await msg.answer(text=text_mess, reply_markup=kb)
        await state.set_state(next_state)


@router.message(ProfileStateFilter())
@user_required
@flags.chat_action("typing")
async def change_name(msg: Message, state: FSMContext, bot: Bot):
    """Изменение имени, фамилии, отчества, даты рождения, веса, пола, роста, имейла"""
    prompt = str(msg.text)
    user_id = msg.from_user.id
    if prompt == 'Отмена':
        await state.set_state(state=StateUserProfile.the_basic_data)
        await msg.answer(text=text_account_basic_datas.account_menu,
                         reply_markup=kb_user_profile.the_basic_data(user_id=user_id))
    else:
        key_state = await state.get_state()
        key = key_state.split(':')[-1]
        check = easy_funcs.check_data_func(key, prompt)
        if check[0]:
            user = User.get_user_by_id(user_id=msg.from_user.id)
            user_basic_data = user.the_basic_data
            up_data = UserBasicData.update({key: prompt}).where(UserBasicData == user_basic_data)
            up_data.execute()
            await state.set_state(StateUserProfile.the_basic_data)
            await msg.answer(text=text_account_basic_datas.update_account_true,
                             reply_markup=kb_user_profile.the_basic_data(user_id=msg.from_user.id))
        else:
            return await msg.answer(text=text_account_basic_datas.err_basic_data_update[key])


@router.message(StateUserProfileBasicData.gender)
@user_required
@flags.chat_action("typing")
async def change_gender(msg: Message, state: FSMContext, bot: Bot):
    """Изменение пола"""
    prompt = msg.text
    user_id = msg.from_user.id
    gen_list = Gender.get_all_names_and_symbols()
    if prompt == 'Отмена':
        await state.set_state(StateUserProfile.the_basic_data)
        await msg.answer(text=text.update_account_cancel,
                         reply_markup=kb_user_profile.the_basic_data(user_id=msg.from_user.id))
    elif prompt in gen_list:
        user = User.get_user_by_id(user_id=user_id)





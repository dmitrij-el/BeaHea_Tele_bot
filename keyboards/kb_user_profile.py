"""
Для удобства работы с ботом реализуется клавиатура.

Интерфейс главного меню.
Интерфейс навигации по профилю

"""

import logging

from aiogram.types import (
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)

from data import db_funcs_user_account, text, text_user_profile
from utils import easy_funcs
from data.models_peewee import Gender, ChannelCom, db_beahea


def choice_delete_account(prompt) -> ReplyKeyboardMarkup:
    choice_delete_account_buttons = [[KeyboardButton(text="Да"),
                                      KeyboardButton(text="Нет")]]
    choice_delete_account_keyboard = ReplyKeyboardMarkup(keyboard=choice_delete_account_buttons,
                                                         resize_keyboard=True,
                                                         input_field_placeholder=prompt)
    return choice_delete_account_keyboard


def user_profile(prompt=text.go_to_point_menu) -> ReplyKeyboardMarkup:
    count = 0
    buttons_questions_menu = [[],[],[]]
    for datas in text_user_profile.question_for_profile.values():
        line = count // 2
        buttons_questions_menu[line].append(KeyboardButton(text=datas[0]))
        count += 1
    buttons_questions_menu[2].append(KeyboardButton(text='Главное меню'))

    buttons_questions_keyboard = ReplyKeyboardMarkup(keyboard=buttons_questions_menu,
                                                     resize_keyboard=True,
                                                     input_field_placeholder=prompt)
    return buttons_questions_keyboard


def user_profile_basic_data(user_id: int) -> ReplyKeyboardMarkup:
    """
    Клавиатура меню "Основных данных" пользователя.

    :param user_id: ID пользователя
    :return: Клавиатура с данными
    """
    profile_basic_data = db_funcs_user_account.user_get_data(user_id=user_id, name_data='user_profile_basic_data')
    if profile_basic_data is None:
        logging.error(f'Не найдет профиль {user_id}')
        user_profile_buttons = [
            [KeyboardButton(text="Что-то пошло не так, аккаунт не найден")]]
    else:
        user_profile_buttons = [[], [], [], []]
        user_data_dict = profile_basic_data.__dict__['__data__']
        print(type(user_data_dict))
        print(user_data_dict)

        ### Здесь остановился. Надо переписать вывод клавиатуры.
        for key, value in user_data_dict.items():
            if type(value) is int:
                user_data_dict[key] = str(value)
            if value is None:
                user_data_dict[key] = text_user_profile.account_basic_data['basic_data_menu'][key]
            else:
                if key == 'gender':
                    gender = Gender.get(Gender.id == user_data_dict[key])
                    user_data_dict['gender'] = gender.symbol
                elif key == 'communication_channels':
                    channel = ChannelCom.get(ChannelCom.id == value)
                    user_data_dict['communication_channels'] = channel.name

        for key, value in user_data_dict.items():
            if key in ['name', 'surname', 'patronymic']:
                user_profile_buttons[0].append(KeyboardButton(text=user_data_dict[key]))
            elif key in ['date_birth', 'gender', 'height', 'weight']:
                user_profile_buttons[1].append(KeyboardButton(text=user_data_dict[key]))
            elif key in ['email', 'phone', 'communication_channels']:
                user_profile_buttons[2].append(KeyboardButton(text=user_data_dict[key]))
        user_profile_buttons[3] = [KeyboardButton(text="Главное меню"), KeyboardButton(text="Назад")]
    user_profile_keyboard = ReplyKeyboardMarkup(keyboard=user_profile_buttons,
                                                resize_keyboard=True,
                                                input_field_placeholder='Выберите соответствующую кнопку.')
    return user_profile_keyboard


def back_button() -> ReplyKeyboardMarkup:
    back_button_buttons = [[KeyboardButton(text="Отмена")]]
    back_button_keyboard = ReplyKeyboardMarkup(keyboard=back_button_buttons,
                                               resize_keyboard=True)
    return back_button_keyboard


def choose_phone() -> ReplyKeyboardMarkup:
    choose_phone_buttons = [[KeyboardButton(text="📞 Отправить телефон", request_contact=True),
                             KeyboardButton(text="Отмена")]]
    choose_phone_keyboard = ReplyKeyboardMarkup(keyboard=choose_phone_buttons,
                                                resize_keyboard=True)
    return choose_phone_keyboard


def choose_communication_channels() -> ReplyKeyboardMarkup:
    button_channels = [[]]
    with db_beahea:
        channels = ChannelCom.select()
        for channel in channels:
            button_channels[0].append(KeyboardButton(text=channel.name))
    button_channels.append([KeyboardButton(text='Отмена')])

    button_channels = ReplyKeyboardMarkup(keyboard=button_channels,
                                          resize_keyboard=True)
    return button_channels


def choose_gender() -> ReplyKeyboardMarkup:
    button_gender = [[]]
    with db_beahea:
        genders = Gender.select()
        for gender in genders:
            button_gender[0].append(KeyboardButton(text=gender.symbol))
    button_gender.append([KeyboardButton(text='Отмена')])

    button_gender_keyboard = ReplyKeyboardMarkup(keyboard=button_gender,
                                                 resize_keyboard=True
                                                 )
    return button_gender_keyboard

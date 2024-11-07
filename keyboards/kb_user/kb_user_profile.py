"""
Для удобства работы с ботом реализуется клавиатура.

Интерфейс главного меню.
Интерфейс навигации по профилю

"""

import logging

from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
)

from datas.models.models_basic_data import UserBasicData, Gender, ChannelCom
from datas.models.models_user import User
from datas.texts import text, text_user_questions, text_account_basic_datas


def choice_delete_account(prompt) -> ReplyKeyboardMarkup:
    choice_delete_account_buttons = [[KeyboardButton(text="Да"),
                                      KeyboardButton(text="Нет")]]
    choice_delete_account_keyboard = ReplyKeyboardMarkup(keyboard=choice_delete_account_buttons,
                                                         resize_keyboard=True,
                                                         input_field_placeholder=prompt)
    return choice_delete_account_keyboard


def user_profile(prompt=text.go_to_point_menu) -> ReplyKeyboardMarkup:
    count = 0
    buttons_questions_menu = [[], []]
    for key, datas in text_user_questions.user_profile.items():
        line = count // 2
        buttons_questions_menu[line].append(KeyboardButton(text=datas[0]))
        count += 1
    buttons_questions_menu[-1].append(KeyboardButton(text='Главное меню'))

    buttons_questions_keyboard = ReplyKeyboardMarkup(keyboard=buttons_questions_menu,
                                                     resize_keyboard=True,
                                                     input_field_placeholder=prompt)
    return buttons_questions_keyboard


def the_basic_data(user_id: int) -> ReplyKeyboardMarkup:
    """
    Клавиатура меню "Основных данных" пользователя.

    :param user_id: ID пользователя
    :return: Клавиатура с данными
    """
    basic_data = UserBasicData.get_as_dict(user_id=user_id)
    count = 0
    user_profile_buttons = [[], [], []]
    for key, value in text_account_basic_datas.basic_data_menu.items():
        count += 1
        if basic_data[key] is None:
            text_kb = value
        else:
            if key == 'gender':
                text_kb = UserBasicData.select().join().where(user_id==user_id).dicts()
                text_kb = text_kb.get()
                print(text_kb)
                text_kb ='text_kb.symbol'
            elif key == 'communication_channels':
                text_kb = basic_data.communication_channels.name
            else:
                text_kb = basic_data[key]
        if count < 4:
            user_profile_buttons[0].append(KeyboardButton(text=text_kb))
        elif count > 5:
            user_profile_buttons[2].append(KeyboardButton(text=text_kb))
        else:
            user_profile_buttons[1].append(KeyboardButton(text=text_kb))

    user_profile_buttons.append([KeyboardButton(text="Главное меню"), KeyboardButton(text="Назад")])
    user_profile_keyboard = ReplyKeyboardMarkup(keyboard=user_profile_buttons,
                                                resize_keyboard=True,
                                                input_field_placeholder='Выберите соответствующую кнопку.')
    return user_profile_keyboard

def the_body_parameters(user_id: int) -> ReplyKeyboardMarkup:
    """
    Клавиатура меню "Основных данных" пользователя.

    :param user_id: ID пользователя
    :return: Клавиатура с данными
    """
    user = User.get_user_by_id(user_id=user_id)
    if user is None:
        logging.error(f'Не найдет профиль {user_id}')
        user_profile_buttons = [[KeyboardButton(text="Что-то пошло не так, аккаунт не найден")]]
    else:
        user_profile_buttons = [[KeyboardButton(text="Главное меню"), KeyboardButton(text="Назад")]]
    user_profile_keyboard = ReplyKeyboardMarkup(keyboard=user_profile_buttons,
                                                resize_keyboard=True,
                                                input_field_placeholder='Выберите соответствующую кнопку.')
    return user_profile_keyboard

def the_questionnaire(user_id: int) -> ReplyKeyboardMarkup:
    """
    Клавиатура меню "Основных данных" пользователя.

    :param user_id: ID пользователя
    :return: Клавиатура с данными
    """
    count = 0
    buttons = [[], []]
    for value in text_user_questions.the_questionnaire.values():
        line = count // 2
        buttons[line].append(KeyboardButton(text=value[0]))
        count += 1
    buttons.append([KeyboardButton(text="Главное меню"), KeyboardButton(text="Назад")])
    keyboard = ReplyKeyboardMarkup(keyboard=buttons,
                                   resize_keyboard=True,
                                   input_field_placeholder='Выберите соответствующую кнопку.')
    return keyboard


def back_button() -> ReplyKeyboardMarkup:
    back_button_buttons = [[KeyboardButton(text="Отмена")]]
    back_button_keyboard = ReplyKeyboardMarkup(keyboard=back_button_buttons,
                                               resize_keyboard=True)
    return back_button_keyboard





"""
Для удобства работы с ботом реализуется клавиатура.

Интерфейс главного меню.
Интерфейс навигации по профилю

"""

import logging

from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)

from data import db_funcs_user_account
from utils import easy_funcs
from data.models_peewee import User, Gender, ChannelCom, City, db_beahea


def main_menu() -> ReplyKeyboardMarkup:
    menu_buttons = [
        [KeyboardButton(text="Телеграм-канал"),
         KeyboardButton(text="👤 Профиль")]
    ]
    menu_keyboard = ReplyKeyboardMarkup(keyboard=menu_buttons,
                                        resize_keyboard=True)
    return menu_keyboard


def user_profile(user_id: int) -> ReplyKeyboardMarkup:
    user_data = db_funcs.user_get_data(user_id=user_id)
    if user_data is None:
        logging.error(f'Не найдет профиль {user_id}')
        user_profile_buttons = [
            [KeyboardButton(text="Что-то пошло не так, аккаунт не найден")]]

    else:
        user_profile_buttons = []
        filter_user_datas = easy_funcs.text_buttons_profile(user_data=user_data)
        for key, value in filter_user_datas.items():
            if key in ['name', 'surname', 'patronymic']:
                user_profile_buttons[0].append(KeyboardButton(text=filter_user_datas[key]))
            elif key in ['date_birth', 'gender', 'height', 'weight']:
                user_profile_buttons[1].append(KeyboardButton(text=filter_user_datas[key]))
            else:
                user_profile_buttons[2].append(KeyboardButton(text=filter_user_datas[key]))

    user_profile_keyboard = ReplyKeyboardMarkup(keyboard=user_profile_buttons,
                                                resize_keyboard=True)
    return user_profile_keyboard


def update_profile_menu() -> ReplyKeyboardMarkup:
    update_profile_menu_buttons = [
        [KeyboardButton(text="Главное меню"),
         KeyboardButton(text="Отменить")]
    ]
    update_profile_menu_keyboard = ReplyKeyboardMarkup(keyboard=update_profile_menu_buttons,
                                                       resize_keyboard=True)
    return update_profile_menu_keyboard


def clear_profile_menu() -> ReplyKeyboardMarkup:
    clear_profile_menu_buttons = [
        [KeyboardButton(text="Главное меню"),
         KeyboardButton(text="Профиль 👥")]
    ]
    clear_profile_menu_keyboard = ReplyKeyboardMarkup(keyboard=clear_profile_menu_buttons,
                                                      resize_keyboard=True)
    return clear_profile_menu_keyboard


def choice_delete_account(prompt) -> ReplyKeyboardMarkup:
    choice_delete_account_buttons = [[KeyboardButton(text="Да"),
                                      KeyboardButton(text="Нет")]]
    choice_delete_account_keyboard = ReplyKeyboardMarkup(keyboard=choice_delete_account_buttons,
                                                         resize_keyboard=True,
                                                         input_field_placeholder=prompt)
    return choice_delete_account_keyboard


def back_button(prompt) -> ReplyKeyboardMarkup:
    back_button_buttons = [[KeyboardButton(text="Отмена")]]
    back_button_keyboard = ReplyKeyboardMarkup(keyboard=back_button_buttons,
                                               resize_keyboard=True,
                                               input_field_placeholder=prompt)
    return back_button_keyboard


def choose_phone(prompt) -> ReplyKeyboardMarkup:
    choose_phone_buttons = [[KeyboardButton(text="📞 Отправить телефон", request_contact=True),
                             KeyboardButton(text="Отмена")]]
    choose_phone_keyboard = ReplyKeyboardMarkup(keyboard=choose_phone_buttons,
                                                resize_keyboard=True,
                                                input_field_placeholder=prompt)
    return choose_phone_keyboard


def choose_communication_channels(prompt) -> ReplyKeyboardMarkup:
    button_channels = [[]]
    with db_beahea:
        channels = ChannelCom.select()
        for channel in channels:
            button_channels[0].append(KeyboardButton(text=channel.name))
    button_channels.append([KeyboardButton(text='Отмена')])

    button_channels = ReplyKeyboardMarkup(keyboard=button_channels,
                                          resize_keyboard=True,
                                          input_field_placeholder=prompt)
    return button_channels


def choose_gender(prompt) -> ReplyKeyboardMarkup:
    button_gender = [[]]
    with db_beahea:
        genders = Gender.select()
        for gender in genders:
            button_gender[0].append(KeyboardButton(text=gender.symbol))
    button_gender.append([KeyboardButton(text='Отмена')])

    button_gender_keyboard = ReplyKeyboardMarkup(keyboard=button_gender,
                                                 resize_keyboard=True,
                                                 input_field_placeholder=prompt)
    return button_gender_keyboard

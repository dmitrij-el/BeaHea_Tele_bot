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


def main_menu() -> ReplyKeyboardMarkup:
    menu_buttons = [
        [KeyboardButton(text="Телеграм-канал"),
         KeyboardButton(text="Частный канал")],
        [KeyboardButton(text="Марафон"),
         KeyboardButton(text="👤 Профиль")]
    ]
    menu_keyboard = ReplyKeyboardMarkup(keyboard=menu_buttons,
                                        resize_keyboard=True,
                                        input_field_placeholder='Выберите соответствующую кнопку.')
    return menu_keyboard


def go_to_telegram_channel() -> InlineKeyboardMarkup:
    telegram_channel_buttons = [
        [InlineKeyboardButton(text='Эля, Еда и Гантеля.', url='t.me/beahea_public')]
    ]
    telegram_channel_keyboard = InlineKeyboardMarkup(inline_keyboard=telegram_channel_buttons)
    return telegram_channel_keyboard


def choice_delete_account(prompt) -> ReplyKeyboardMarkup:
    choice_delete_account_buttons = [[KeyboardButton(text="Да"),
                                      KeyboardButton(text="Нет")]]
    choice_delete_account_keyboard = ReplyKeyboardMarkup(keyboard=choice_delete_account_buttons,
                                                         resize_keyboard=True,
                                                         input_field_placeholder=prompt)
    return choice_delete_account_keyboard


def back_button() -> ReplyKeyboardMarkup:
    back_button_buttons = [[KeyboardButton(text="Отмена")]]
    back_button_keyboard = ReplyKeyboardMarkup(keyboard=back_button_buttons,
                                               resize_keyboard=True)
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


def user_profile(prompt=text.go_to_point_menu) -> ReplyKeyboardMarkup:
    buttons_questions_menu = []
    for datas in text_user_profile.question_for_profile.values():
        buttons_questions_menu.append([KeyboardButton(text=datas[0])])
    buttons_questions_menu.append([KeyboardButton(text='Главное меню')])

    buttons_questions_keyboard = ReplyKeyboardMarkup(keyboard=buttons_questions_menu,
                                                     resize_keyboard=True,
                                                     input_field_placeholder=prompt)
    return buttons_questions_keyboard


def user_profile_basic_data(user_id: int) -> ReplyKeyboardMarkup:
    user_profile_basic_data = db_funcs_user_account.user_get_data(user_id=user_id, name_data='user_profile_basic_data')
    if user_profile_basic_data is None:
        logging.error(f'Не найдет профиль {user_id}')
        user_profile_buttons = [
            [KeyboardButton(text="Что-то пошло не так, аккаунт не найден")]]
    else:
        user_profile_buttons = [[], [], [], []]
        filter_user_datas = easy_funcs.text_buttons_profile(user_data=user_profile_basic_data)
        for key, value in filter_user_datas.items():
            if key in ['name', 'surname', 'patronymic']:
                user_profile_buttons[0].append(KeyboardButton(text=filter_user_datas[key]))
            elif key in ['date_birth', 'gender', 'height', 'weight']:
                user_profile_buttons[1].append(KeyboardButton(text=filter_user_datas[key]))
            elif key in ['email', 'phone', 'communication_channels']:
                user_profile_buttons[2].append(KeyboardButton(text=filter_user_datas[key]))
        user_profile_buttons[3] = [KeyboardButton(text="Главное меню"), KeyboardButton(text="Назад")]
    user_profile_keyboard = ReplyKeyboardMarkup(keyboard=user_profile_buttons,
                                                resize_keyboard=True,
                                                input_field_placeholder='Выберите соответствующую кнопку.')
    return user_profile_keyboard

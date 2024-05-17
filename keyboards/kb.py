import logging

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)

from Tbot_beahea.data import db_funcs
from Tbot_beahea.data import text
from Tbot_beahea.utils import easy_funcs

"""
Для удобства работы с ботом реализуется клавиатура, которая хранится здесь.

"""


def main_menu() -> InlineKeyboardMarkup:
    menu = [
        [InlineKeyboardButton(text="📣 Телеграм-канал", callback_data="telegram_pub_channel"),
        InlineKeyboardButton(text="㊙️ Частный канал связи", callback_data="private_channel")],
        [InlineKeyboardButton(text="👤 Профиль ", callback_data="user_profile"),
        InlineKeyboardButton(text="Калькуляторы", callback_data="calculators")],
        [InlineKeyboardButton(text="🏋️ Услуги", callback_data="price"),
        InlineKeyboardButton(text="⁉️ Информация", callback_data="info")]
    ]
    menu = InlineKeyboardMarkup(inline_keyboard=menu)
    return menu





def user_profile(user_id: int) -> InlineKeyboardMarkup:
    user_data = db_funcs.user_get_data(user_id=user_id)
    if user_data is None:
        logging.error(f'Не найдет профиль {user_id}')
        user_profile = [[InlineKeyboardButton(text="Что-то пошло не так, аккаунт не найден", callback_data="creat_error_profile")]]

    else:
        filter_user_datas = easy_funcs.text_buttons_profile(user_data=user_data)
        print(filter_user_datas)


        user_profile = [
                [InlineKeyboardButton(text="{name}".format(name=filter_user_datas['name']), callback_data="change_name"),
                InlineKeyboardButton(text="{surname}".format(surname=filter_user_datas['surname']), callback_data="change_surname"),
                InlineKeyboardButton(text="{patronymic}".format(patronymic=filter_user_datas['patronymic']), callback_data="change_patronymic")],
                [InlineKeyboardButton(text="{date_birth}".format(date_birth=filter_user_datas['date_birth']), callback_data="change_date_birth"),
                InlineKeyboardButton(text="{gender}".format(gender=filter_user_datas['gender']), callback_data="change_gender")],
                [InlineKeyboardButton(text="{height} (см)".format(height=filter_user_datas['height']), callback_data="change_height"),
                InlineKeyboardButton(text="{weight} (кг)".format(weight=filter_user_datas['weight']), callback_data="change_weight")],
                [InlineKeyboardButton(text="{email}".format(email=filter_user_datas['email']), callback_data="change_email"),
                InlineKeyboardButton(text="{phone}".format(phone=filter_user_datas['phone']), callback_data="change_phone")],
                [InlineKeyboardButton(text="{communication_channels}".format(communication_channels=filter_user_datas['communication_channels']),
                                      callback_data="change_communication_channels")],
                [InlineKeyboardButton(text="Главное меню", callback_data="menu")]
            ]


    user_profile = InlineKeyboardMarkup(inline_keyboard=user_profile)
    return user_profile

def update_profile_menu() -> InlineKeyboardMarkup:
    update_profile_menu = [
        [InlineKeyboardButton(text="Главное меню", callback_data="menu"),
        InlineKeyboardButton(text="Отменить", callback_data="user_profile")]
    ]
    update_profile_menu = InlineKeyboardMarkup(inline_keyboard=update_profile_menu)
    return update_profile_menu

def clear_profile_menu() -> InlineKeyboardMarkup:
    clear_profile_menu = [
        [InlineKeyboardButton(text="Главное меню", callback_data="menu"),
        InlineKeyboardButton(text="Профиль 👥", callback_data="user_profile")]
    ]
    clear_profile_menu = InlineKeyboardMarkup(inline_keyboard=clear_profile_menu)
    return clear_profile_menu


def choiceYN(prompt) -> ReplyKeyboardMarkup:
    choiceYN = [[KeyboardButton(text="Да"),
                KeyboardButton(text="Нет")]]
    choiceYN = ReplyKeyboardMarkup(keyboard=choiceYN,
                                   resize_keyboard=True,
                                   input_field_placeholder=prompt)
    return choiceYN


def back_button(prompt) -> ReplyKeyboardMarkup:
    back_button = [[KeyboardButton(text="Отмена")]]
    back_button = ReplyKeyboardMarkup(keyboard=back_button,
                                   resize_keyboard=True,
                                   input_field_placeholder=prompt)
    return back_button


iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
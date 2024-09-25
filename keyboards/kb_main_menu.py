"""
Для удобства работы с ботом реализуется клавиатура.

Интерфейс главного меню.
Интерфейс навигации по профилю

"""

from aiogram.types import (
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup
)

from data import db_funcs_user_account, text, text_user_profile, text_of_paid_service
from utils import easy_funcs
from data.models_peewee import Gender, ChannelCom, db_beahea
from states.states import StateMenu


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

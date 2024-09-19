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


def go_to_private_telegram_channel() -> ReplyKeyboardMarkup:
    telegram_channel_buttons = [
        [InlineKeyboardButton(text='Купить подписку на частный канал', url='t.me/beahea_public')]
    ]
    telegram_channel_keyboard = InlineKeyboardMarkup(inline_keyboard=telegram_channel_buttons)
    return telegram_channel_keyboard


def go_to_marathon_channel() -> InlineKeyboardMarkup:
    telegram_channel_buttons = [
        [InlineKeyboardButton(text='Купить марафон мечты')]
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



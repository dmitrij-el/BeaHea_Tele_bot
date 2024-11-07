import logging

from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
)

from datas.models.models_basic_data import ChannelCom, Gender
from datas.models.models_db import db_beahea

def communication_channels() -> ReplyKeyboardMarkup:
    button_channels = [[]]
    with db_beahea:
        channels = ChannelCom.select()
        for channel in channels:
            button_channels[0].append(KeyboardButton(text=channel.name))
    button_channels.append([KeyboardButton(text='Отмена')])

    button_channels = ReplyKeyboardMarkup(keyboard=button_channels,
                                          resize_keyboard=True)
    return button_channels


def gender() -> ReplyKeyboardMarkup:
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


def phone() -> ReplyKeyboardMarkup:
    choose_phone_buttons = [[KeyboardButton(text="📞 Отправить телефон", request_contact=True),
                             KeyboardButton(text="Отмена")]]
    choose_phone_keyboard = ReplyKeyboardMarkup(keyboard=choose_phone_buttons,
                                                resize_keyboard=True)
    return choose_phone_keyboard



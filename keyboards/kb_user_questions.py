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


def user_redactor_question_for_profile(user_id, prompt=text.go_to_point_menu) -> ReplyKeyboardMarkup:

    redactor_question_buttons = [
        [KeyboardButton(text="Посмотреть ответы"), KeyboardButton(text="Редактировать ответы")],
        [KeyboardButton(text='Назад')]
    ]
    redactor_question_keyboard = ReplyKeyboardMarkup(keyboard=redactor_question_buttons,
                                                     resize_keyboard=True,
                                                     input_field_placeholder=prompt)
    return redactor_question_keyboard


def user_question(user_id, prompt=text.go_to_point_menu) -> ReplyKeyboardMarkup:

    redactor_question_buttons = [
        [KeyboardButton(text="Посмотреть ответы"), KeyboardButton(text="Редактировать ответы")],
        [KeyboardButton(text='Назад')]
    ]
    redactor_question_keyboard = ReplyKeyboardMarkup(keyboard=redactor_question_buttons,
                                                     resize_keyboard=True,
                                                     input_field_placeholder=prompt)
    return redactor_question_keyboard

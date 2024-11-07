from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
)

from datas.texts import text_user_questions, text


def user_menu_question_for_profile(user_id, prompt=text.go_to_point_menu) -> ReplyKeyboardMarkup:
    redactor_question_buttons = [
        [KeyboardButton(text="Посмотреть ответы"), KeyboardButton(text="Редактировать ответы")],
        [KeyboardButton(text='Назад')]
    ]
    redactor_question_keyboard = ReplyKeyboardMarkup(keyboard=redactor_question_buttons,
                                                     resize_keyboard=True,
                                                     input_field_placeholder=prompt)
    return redactor_question_keyboard


def user_redactor_question_for_profile(user_id, nums_questions, prompt=text.go_to_point_menu) -> ReplyKeyboardMarkup:
    n = 3 if nums_questions <= 6 else 4
    rows = nums_questions // n + (1 if nums_questions % n else 0)

    redactor_question_buttons = [[] for _ in range(rows)]
    for i in range(nums_questions):
        line = i // n
        redactor_question_buttons[line].append(KeyboardButton(text=str(i)))
    redactor_question_buttons.append([KeyboardButton(text='Назад'),
                                      KeyboardButton(text='Главное меню')])
    redactor_question_keyboard = ReplyKeyboardMarkup(keyboard=redactor_question_buttons,
                                                     resize_keyboard=True,
                                                     input_field_placeholder=prompt)
    return redactor_question_keyboard


def user_question(user_id, prompt=text.go_to_point_menu) -> ReplyKeyboardMarkup:
    redactor_question_buttons = [
        [KeyboardButton(text="Назад"), KeyboardButton(text="Главное меню")]
    ]
    redactor_question_keyboard = ReplyKeyboardMarkup(keyboard=redactor_question_buttons,
                                                     resize_keyboard=True,
                                                     input_field_placeholder=prompt)
    return redactor_question_keyboard

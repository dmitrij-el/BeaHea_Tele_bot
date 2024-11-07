from datetime import date, timedelta, datetime
from functools import wraps

from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
)
from datas.models.models_user import Admin


def admin_required_kb(func):
    @wraps(func)
    def wrapper(user_id: int, *args, **kwargs):
        if Admin.is_admin(user_id=user_id):
            return func(user_id, *args, **kwargs)
        else:
            menu_buttons = [[KeyboardButton(text="Главное меню")]]
            menu_keyboard = ReplyKeyboardMarkup(keyboard=menu_buttons,
                                                resize_keyboard=True,
                                                input_field_placeholder='Выберите соответствующую кнопку.')
            return menu_keyboard

    return wrapper


@admin_required_kb
def admin_main_menu(user_id: int) -> ReplyKeyboardMarkup:
    menu_buttons = [
        [KeyboardButton(text="Администраторы")],
        [KeyboardButton(text="Главное меню")]
    ]
    menu_keyboard = ReplyKeyboardMarkup(keyboard=menu_buttons,
                                        resize_keyboard=True,
                                        input_field_placeholder='Выберите соответствующую кнопку.')
    return menu_keyboard


@admin_required_kb
def admin_cancel(user_id: int) -> ReplyKeyboardMarkup:
    adm_cancel_buttons = [[KeyboardButton(text="Отмена")]]
    adm_cancel_keyboard = ReplyKeyboardMarkup(keyboard=adm_cancel_buttons,
                                              resize_keyboard=True,
                                              input_field_placeholder='Убедитесь в правильности ввода.')
    return adm_cancel_keyboard


@admin_required_kb
def admin_load_or_cancel(user_id: int) -> ReplyKeyboardMarkup:
    admin_load_or_cancel_buttons = [[KeyboardButton(text="Загрузить"),
                                     KeyboardButton(text="Отмена")]]
    admin_load_or_cancel_keyboard = ReplyKeyboardMarkup(keyboard=admin_load_or_cancel_buttons,
                                                        resize_keyboard=True,
                                                        input_field_placeholder='Убедитесь в правильности ввода.')
    return admin_load_or_cancel_keyboard


@admin_required_kb
def admin_yes_no(user_id: int) -> ReplyKeyboardMarkup:
    adm_yes_no_buttons = [[KeyboardButton(text="Да"),
                           KeyboardButton(text="Нет")]]
    adm_yes_no_keyboard = ReplyKeyboardMarkup(keyboard=adm_yes_no_buttons,
                                              resize_keyboard=True,
                                              input_field_placeholder='Выберите соответствующую кнопку.')
    return adm_yes_no_keyboard


@admin_required_kb
def admin_add_del_back(user_id: int) -> ReplyKeyboardMarkup:
    adm_add_del_back_buttons = [
        [KeyboardButton(text="Добавить"),
         KeyboardButton(text="Удалить")],
        [KeyboardButton(text="Назад")]
    ]
    adm_add_del_back_keyboard = ReplyKeyboardMarkup(keyboard=adm_add_del_back_buttons,
                                                    resize_keyboard=True,
                                                    input_field_placeholder='Выберите соответствующую '
                                                                            'кнопку.')
    return adm_add_del_back_keyboard


@admin_required_kb
def admin_date_enter(user_id: int, day_date: datetime = None, weeks_fnc: bool = False) -> ReplyKeyboardMarkup:
    admin_date_enter_buttons = [[], []]
    if day_date is None:
        date_date = date.today()
    else:
        date_date = day_date
    for i in range(6):
        date_text = date_date.strftime('%d-%m-%Y %a')
        if i < 3:
            admin_date_enter_buttons[0].append(KeyboardButton(text=date_text))
        else:
            admin_date_enter_buttons[1].append(KeyboardButton(text=date_text))
        if weeks_fnc:
            date_date += timedelta(weeks=1)
        else:
            date_date += timedelta(days=1)
    admin_date_enter_buttons.append([KeyboardButton(text="Отмена")])
    admin_date_enter_keyboard = ReplyKeyboardMarkup(keyboard=admin_date_enter_buttons,
                                                    resize_keyboard=True,
                                                    input_field_placeholder='Убедитесь в правильности ввода.')
    return admin_date_enter_keyboard

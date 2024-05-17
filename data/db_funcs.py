"""Набор функций для работы с базами данных"""
import logging
from typing import Coroutine
from Tbot_beahea.data import text, models
from Tbot_beahea.keyboards import kb
from Tbot_beahea.utils import easy_funcs
from Tbot_beahea.data.models import User, Gender, db_beahea




def check_user_datas(user_id: str) -> bool:
    """Проверка БД на наличие пользователя"""
    try:
        with db_beahea:
            user = User.select().where(User.user_id == user_id).get()
        if user:
            return True
        else:
            return False
    except Exception as exp:
        logging.error(f'В процессе проверки на наличие пользователя произошла непредвиденная ошибка\n'
                      f'Ошибка: {exp}')
        return False




def user_get_data(user_id: str) -> User:
    """Подкачка данных пользователя из БД по ключу"""
    try:
        with db_beahea:
            user = User.select().where(User.user_id == user_id).get()
        return user
    except Exception as exp:
        logging.error(f'В процессе загрузки данных пользователя {user_id} произошла непредвиденная ошибка\n'
                      f'Ошибка: {exp}')




def user_rec_datas_in_reg(acc_dict: dict) -> bool:
    """Запись данных профиля в БД при регистрации"""
    try:
        with db_beahea.atomic():
            User.create(**acc_dict)
        return True
    except Exception as exp:
        logging.error(f'В процессе записи пользователя {acc_dict["user_id"]} в БД произошла непредвиденная ошибка\n'
                      f'Ошибка: {exp}')
        return False


def user_delete_datas(user_id: str) -> bool:
    """Удаление данных пользователя из БД"""
    try:
        with db_beahea:
            User.delete_instance(User.user_id == user_id)
        return True
    except Exception as exp:
        logging.error(f'В процессе удаления пользователя {user_id} произошла непредвиденная ошибка\n'
                      f'Ошибка: {exp}')
        return False


def user_update_data(user_id: str, column_datas: str, data: str|int|bool) -> bool:
    """
    Функция обновления данных пользователя с фильтрами.

    :param user_id: ID пользователя
    :param column_datas: Имя обновляемой колонки
    :param data: Новые данные
    :return: True при удачном обновление, иначе False
    """
    try:
        with db_beahea:
            User.update({column_datas: data}).where(User.user_id == user_id)
    except Exception as exp:
        logging.error(f'В процессе обновления данных пользователя {user_id} по ключу произошла непредвиденная ошибка\n'
                      f'Ошибка: {exp}')
        return False


async def change_datas(msg, change_data: str) -> Coroutine:
    """
    Асинхронная функция является центральной при данных профиля пользователем.
    Она производит проверку данных с помощью electoral_func.
    Также предлагает отменить с помощью кнопки действие.

    :param msg: Чат
    :param change_data: Имя изменяемых данных

    :rtype: Coroutine
    """
    prompt = msg.text
    check_name_electoral = easy_funcs.electoral_func(change_data, prompt)
    if prompt == 'Отмена':
        await msg.answer(text.update_account_cancel, reply_markup=kb.ReplyKeyboardRemove())
        await msg.answer(text=text.account_menu,
                         reply_markup=kb.user_profile(user_id=msg.from_user.id))
    elif check_name_electoral is False:
        await msg.answer(check_name_electoral[1], reply_markup=kb.user_profile(user_id=msg.from_user.id))
    else:
        mesg = await msg.answer(text=text.update_profile_wait)
        user_id=msg.from_user.id
        update_func = user_update_data(user_id=user_id, column_datas=change_data, data=prompt)
        if update_func:
            await mesg.answer(text=text.update_account_true,
                              reply_markup=kb.ReplyKeyboardRemove())
        else:
            await mesg.answer(text=text.update_account_false,
                              reply_markup=kb.ReplyKeyboardRemove())
        await msg.answer(text.account_menu, reply_markup=kb.user_profile(user_id=msg.from_user.id))
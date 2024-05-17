import pymorphy3
import re

from Tbot_beahea.data import text, models
from Tbot_beahea.data.models import User


def gender_func(*args: list) -> str:
    """
    Функция принимает данные для определения пола человека с помощью библиотеки pymorphy3
    :param args: Список с данными для определения пола

    :return: Одно из трех значений (men - мужской пол, women - женский, unknown - определить не удалось
    :rtype: str
    """
    masc = 0
    femn = 0
    for name in args:
        if name is not None:
            parsed_word = pymorphy3.MorphAnalyzer().parse(name)[0].tag.gender
            if parsed_word == "masc":
                masc += 1
            elif parsed_word == "femn":
                femn += 1
    if masc > femn:
        return "men"
    elif masc < femn:
        return "women"
    else:
        return None

def text_buttons_profile(user_data: models.User) -> tuple:

    """
    Функция для формирования текстового интерфейса клавиатуры в меню профиля

    :param user_data: Вводные данные из базы данных
    :return:
    """

    user_data_dict = user_data.__dict__['__data__']

    if user_data.gender == None:
        user_data_dict['gender'] = 'Пол'

    if user_data.name == None:
        user_data_dict['name'] = 'Имя'

    if user_data.surname == None:
        user_data_dict['surname'] = 'Фамилия'

    if user_data.patronymic == None:
        user_data_dict['patronymic'] = 'Отчество'

    if user_data.date_birth == None:
        user_data_dict['date_birth'] = 'Дата рождения'

    if user_data.height == None:
        user_data_dict['height'] = 'Рост'

    if user_data.weight == None:
        user_data_dict['weight'] = 'Вес'

    if user_data.email == None:
        user_data_dict['email'] = 'Email'

    if user_data.phone == None:
        user_data_dict['phone'] = 'Телефон'

    if user_data.communication_channels == None:
        user_data_dict['communication_channels'] = 'Канал связи'


    return user_data_dict




def electoral_func(electoral: str|int, mesg: str) -> bool|str:

    """
    Функция проверки ввода данных аккаунта

    :param electoral: Название метода проверки
    :param mesg: Текстовое сообщение для проверки на соответствие

    :return:
    :rtype: bool, (str)
    """
    if electoral in ['user_name', 'user_surname', 'user_patronymic']:
        if len(mesg) > 63:
            return False, text.err_change_name
    elif electoral == 'date_birth':
        if len(mesg) > 63:
            return False, text.err_change_date_birth
    elif electoral == 'gender':
        if mesg.lower() not in ['men', 'women']:
            return False, text.err_change_gender
    elif electoral == 'height':
        if 30 > int(mesg) > 250:
            return False, text.err_change_height
    elif electoral == 'weight':
        if 20 > int(mesg) > 64:
            return False, text.err_change_weight
    elif electoral == 'email':
        if not checking_data_expression(email=mesg):
            return False, text.err_change_email
    elif electoral == 'phone':
        if not checking_data_expression(phone_number=mesg):
            return False, text.err_change_phone
    elif electoral == 'communication_channel':
        if len(mesg) > 64:
            return False, text.err_change_communication_channels

def checking_data_expression(data: str,
                             phone_number=False,
                             email=False,
                             date_birth=False) -> bool:
    '''
    Проверка данных с помощью регулярных выражений. Выберите переменную из списка\n
    Номера телефона: phone_number\n
    Адреса электронной почты: email\n
    Имени пользователя: user_name

    :param data: Данные для проверки на соответствие
    :type data: (str)

    :return: Сравнивает и возвращает True или False
    :rtype: bool
    '''


    expressions_dir = {
        'date_birth':
            r'[1-9]{1}\d{0,1}',
        'phone_number':
            r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
        'email':
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    }


    if date_birth:
        expression = expressions_dir["date_birth"]
    elif phone_number:
        expression = expressions_dir["phone_number"]
    elif email:
        expression = expressions_dir["email"]

    result = re.compile(expression)
    if result.search(str(data)):
        return True
    else:
        return False



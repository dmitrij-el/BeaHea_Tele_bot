import re

from datas.texts import text, text_account_basic_datas
from datas.models.models_basic_data import Gender, ChannelCom

def checking_data_expression(phone_number: str | bool = False,
                             email: str | bool = False,
                             date_birth: str | bool = False,
                             time: str | bool = False,
                             date_day: str | bool = False) -> bool:
    """
    Проверка данных с помощью регулярных выражений. Выберите переменную из списка\n
    Номера телефона: phone_number\n
    Адреса электронной почты: email\n
    Имени пользователя: user_name

    :param phone_number: Номер телефона пользователя

    :param email: Адрес электронной почты пользователя

    :param date_birth: Дата рождения пользователя

    :return: Сравнивает и возвращает True или False
    """

    expressions_dir = {
        'date_birth':
            r'(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d',
        'phone_number':
            r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
        'date':
            r'(19|20)\d\d[- /.,;:](0[1-9]|1[012])[- /.,;:](0[1-9]|[12][0-9]|3[01])',
        'time':
            r'^([0-1]?[0-9]|2[0-3])[:;.-/, ][0-5][0-9]',
        'email':
            r'^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$',
        'number_credit_card':
            r'[0-9]{13,16}'
    }
    expression = ''
    data = ''

    if date_birth:
        expression = expressions_dir["date_birth"]
        data = date_birth
    elif phone_number:
        expression = expressions_dir["phone_number"]
        data = phone_number
    elif email:
        expression = expressions_dir["email"]
        data = email
    elif time:
        expression = expressions_dir["time"]
        data = time
    elif date_day:
        expression = expressions_dir["date"]
        data = date_day

    result = re.compile(expression)
    if result.search(str(data)):
        return True
    else:
        return False


def correction_datas(phone_number: str = None,
                     date_day: str = None,
                     time: str = None) -> str:
    if phone_number:
        ans = ''.join(re.findall(r'\b\d+\b', phone_number))
        if ans[0] == '7':
            ans = '+' + ans
        elif ans[0] == '8':
            ans = '+7' + ans.lstrip('8')
        elif ans[0] == '9':
            ans = '+7' + ans
        return ans
    elif date_day:
        ans = (re.findall(r'\b\d+\b', date_day))
        if len(ans[-1]) > len(ans[0]):
            ans[0], ans[-1] = ans[-1], ans[0]
        ans = '-'.join(ans)
        return ans
    elif time:
        ans = ':'.join(re.findall(r'\b\d+\b', time))
        return ans


def check_data_func(key: str | int, mess: str) -> [bool, str]:
    """
    Функция проверки ввода данных аккаунта

    :param key: Название метода проверки

    :param mess: Текстовое сообщение для проверки на соответствие

    :return: Объект с информацией о результате проверки
    """
    if key in ['name', 'surname', 'patronymic']:
        if len(mess) > 63:
            return (False,
                    text_account_basic_datas.err_basic_data_update[key])
    elif key == 'date_birth':
        return (checking_data_expression(date_birth=mess),
                text_account_basic_datas.err_basic_data_update[key])
    elif key == 'email':
        return (checking_data_expression(email=mess),
                text_account_basic_datas.err_basic_data_update[key])
    elif key == 'phone':
        return (checking_data_expression(phone_number=mess),
                text_account_basic_datas.err_basic_data_update[key])
    elif key == 'communication_channels':
        ans_list = [[i.name, i.symbol] for i in ChannelCom.select(ChannelCom.name, ChannelCom.symbol)]
        answer_list = []
        for ans in ans_list:
            for i in ans:
                answer_list.append(i)
        if not mess.title() in answer_list:
            return (False,
                    text_account_basic_datas.err_basic_data_update[key])
    elif key == 'gender':
        ans_list = [[i.name, i.symbol] for i in Gender.select(Gender.name, Gender.symbol)]
        answer_list = []
        for ans in ans_list:
            for i in ans:
                answer_list.append(i)
        if not mess.title() in answer_list:
            return (False,
                    text_account_basic_datas.err_basic_data_update[key])
    return True, text.update_account_true
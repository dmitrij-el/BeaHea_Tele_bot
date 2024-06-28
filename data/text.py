"""Сборник текстов для интерфейса взаимодействия с пользователем"""

greet_cont = """Приветствую в телеграм боте Элеоноры - тренера и нутрициолога.
Пишу о том, как быть круглый год в хорошей форме, здоровым и весёлым-)
Чтобы посмотреть команды, введите /help"""

menu = "📍 Главное меню"
go_to_telegram_channel = """Посетите мой публичный телеграм-канал. Там много интересного."""
go_to_point_menu = ('Для лучшего анализа предоставьте актуальные данные. '
                    'В данном разделе хранятся все ваши данные. Для перехода выберите соответствующий пункт меню')



account_menu_1 = 'Ваш профиль.'
account_menu_2 = 'Для изменения нажмите на соответствующую кнопку'
account_qst_clear = 'У вас уже есть профиль, хотите его очистить?'
account_rec_datas = 'Подождите, данные записываются.'
clear_account_question = 'Хотите сбросить профиль?'
clear_account_true = 'Аккаунт очищен.'
clear_account_wait = 'Идет удаление аккаунта...'
clear_account_cancel = 'Очистка аккаунта отменена.'
update_profile_wait = 'Идет обновление данных...'
update_account_true = 'Обновление данных прошло успешно.'
update_account_false = 'При обновлении данных произошла ошибка.'
update_profile_enter_data = 'Введите новые данные.'
update_account_cancel = 'Изменение данных отменено.'
update_gender = 'Выберите ваш пол.'
update_communication_channels = 'Выберите предпочтительный канал связи.'
update_phone = 'Поделитесь своим контактом или введите номер телефона вручную.'
update_email = 'Введите email.'
profile_name = 'Ваше имя {user_name}'
profile_surname = 'Ваша фамилия {user_surname}'
profile_patronymic = 'Ваше отчество {user_patronymic}'
profile_date_birth = 'Ваша дата рождения {date_birth}'
profile_gender = 'Ваш пол {gender}'
profile_height = 'Ваш рост {height} см'
profile_weight = 'Ваш вес {weight} кг'
profile_email = 'Ваш email {email}'
profile_phone = 'Ваш телефон {phone}'
profile_communication_channel = 'Канал связи {communication_channel}'


err = "🚫 К сожалению произошла ошибка, попробуйте позже"
err_reg_fatal = """Произошла критическая ошибка при регистрации. Уведомите пожалуйста администратора.
Следующее сообщение будет отправлено администратору."""
err_err_change = '\nЕсли вы считаете что ошибки нету, просим написать администратору в личку.'
err_change_name = 'Ошибка. Для имени можно использовать любой набор символов менее 64 букв.' + err_err_change
err_change_date_birth = 'Ошибка. Дата рождения в формате ДД.ММ.ГГГГ или ДД/ММ/ГГГГ.' + err_err_change
err_change_gender = ('Ошибка. Для выбора пола воспользуйтесь кнопками ниже, или введите: '
                     '\n"men" - мужской, '
                     '\n"woman" - женский' + err_err_change
                     )
err_change_height = 'Ошибка. Укажите рост в сантиметрах.' + err_err_change
err_change_weight = 'Ошибка. Укажите вес в килограммах.' + err_err_change
err_change_email = 'Ошибка. Формат адреса электронной почты user@host.domain' + err_err_change
err_change_phone = 'Ошибка. Некорректный номер телефона' + err_err_change
err_change_communication_channels = ('Ошибка. Для выбора пола воспользуйтесь кнопками ниже, или введите: '
                                     '\n"telegram" - Telegram'
                                     '\n"discord" - Дискорд'
                                     '\n"email" - Почта'
                                     '\n"phone" - Мобильная связь' + err_err_change
                                     )

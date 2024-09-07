from states.states import (StateUserProfileTrain,
                           StateUserProfileGoals,
                           StateUserProfileQuestionnaire,
                           StateUserProfileBasicData,
                           StateUserProfileLimitsFactors,
                           StateUserProfile)
from data.models_peewee import UserProfileBasicData
from keyboards import kb_user_profile

the_questionnaire_questions = dict(
    question_number_of_meals=['Сколько раз в день приём пищи, включая перекусы.',
                              StateUserProfileQuestionnaire.question_number_of_meals],
    question_diagnosis_high_low_pressure=[
        'Диагностировали ли Вам проблемы с сердцем или высокое артериальное давление?',
        'Да', 'Нет',
        StateUserProfileQuestionnaire.question_diagnosis_high_low_pressure],
    question_diagnosis_chronic_disease=['Диагностировали ли вам когда-нибудь какое-то иное  хроническое заболевание?',
                                        'Да', 'Нет',
                                        StateUserProfileQuestionnaire.question_diagnosis_chronic_disease],
    question_diagnosis_fainting=['Были ли у вас потеря равновесия, обмороки или потеря сознания из-за головокружения '
                                 'за последние 12 месяцев? (ответьте "Нет", если головокружение было'
                                 'вызвано гипервентиляцией, в том числе во время интенсивной физической активности)',
                                 'Да', 'Нет',
                                 StateUserProfileQuestionnaire.question_diagnosis_fainting],
    question_problem_musculoskeletal_system=['Есть ли у вас проблемы с опорно-двигательной системой (мышцами, связками,'
                                             'суставами, сухожилиями, костями), которые можно усугубить,'
                                             'повысив уровень вашей физической активности? (Ответьте "Нет", если такие'
                                             'проблемы были в прошлом, но не беспокоят в настоящее время и не мешают'
                                             'активному образу жизни)',
                                             'Да', 'Нет',
                                             StateUserProfileQuestionnaire.question_problem_musculoskeletal_system],
    question_physical_activity_restrictions=['Говорил ли вам лечащий врач, что у вас какие-то ограничения или'
                                             'противопоказания по физическим нагрузкам?',
                                             'Да', 'Нет',
                                             StateUserProfileQuestionnaire.question_physical_activity_restrictions],
    question_taking_medications=['Принимаете ли вы в настоящее время  лекарства от каких-то хронических заболеваний?',
                                 'Да', 'Нет', StateUserProfileQuestionnaire.question_taking_medications],
    question_injuries_with_intervention=['Были ли у Вас в прошлом травмы, которые потребовали операции или которые вам'
                                         'предлагали лечить оперативным путем?',
                                         'Да', 'Нет', StateUserProfileQuestionnaire.question_injuries_with_intervention]
)

the_goals_questions = dict(
    question_list_of_goals=['Отметьте все цели, которые имеют для Вас значение',
                            'Набор мышечной массы',
                            'Уменьшение жирового компонента массы тела',
                            'Поддержание формы',
                            'Повышение уровня энергии и работоспособности',
                            'Повышение физической подготовленности',
                            'Формирование стабильных пищевых привычек',
                            'Формирование привычки к регулярным физическим нагрузкам',
                            'Избавление от хронических болей',
                            'Овладение сложными двигательными навыками',
                            StateUserProfileGoals.question_list_of_goals],
    question_one_goal_from_list=['Какая из перечисленных целей является наиболее важной?',
                                 StateUserProfileGoals.question_one_goal_from_list],
    question_formulate_goal=['Сформулируйте эту цель как можно конкретнее (что конкретно и насколько хотите изменить)',
                             StateUserProfileGoals.question_formulate_goal],
    question_reasons_goal=['Напишите причины, почему эта цель является для Вас важной. Постарайтесь ответить подробно',
                           StateUserProfileGoals.question_reasons_goal],
    question_actions_to_achieve_the_goal=['Предпринимали ли Вы уже какие-то действия для достижения этой цели?'
                                          ' Если да, то какие?',
                                          StateUserProfileGoals.question_actions_to_achieve_the_goal],
    question_obstacles_on_the_way=['Какие препятствия Вы встречали на пути к этой цели?',
                                   StateUserProfileGoals.question_obstacles_on_the_way],
    question_help_to_the_goal=['Вам нужна помощь на пути к этой цели? В чём она заключается?'
                               '(Какие возможные проблемы вы хотите решить с помощью специалиста)?',
                               StateUserProfileGoals.question_help_to_the_goal],
    question_weight_5_year=['Что происходило с Вашим весом за последние 5 лет?',
                            'Стабилен',
                            'Каждый год немного увеличивается',
                            'Резко растёт',
                            'Вес снижается', StateUserProfileGoals.question_weight_5_year])

the_trane_questions = dict(
    question_exp_weight_training=['Каков Ваш опыт тренировок с отягощениями?',
                                  'Опыта регулярных тренировок с отягощениями нет',
                                  'Есть опыт регулярных тренировок с отягощениями, но без '
                                  'тренера и/или четкого структурированного плана',
                                  'Опыт регулярных тренировок с отягощениями по '
                                  'структурированной программе от 6 месяцев до 2 лет',
                                  'Опыт регулярных тренировок с отягощениями по '
                                  'структурированной программе 2 года и более',
                                  StateUserProfileTrain.question_exp_weight_training],
    question_regularly_train_at_the_moment=[
        'Насколько регулярно Вы тренируетесь в настоящее время?',
        'Последняя тренировка была более месяца назад или это будет первая тренировка',
        '1-3 раза в неделю, с пропусками и нерегулярно',
        '2-5 раз в неделю в течение нескольких месяцев или более',
        StateUserProfileTrain.question_regularly_train_at_the_moment],
    question_volume_every_day_activity=['Каков Ваш текущий уровень ежедневной активности?',
                                        'Низкий уровень активности (офисная работа, сидячий образ жизни)',
                                        'Средний уровень активности (активный отдых, периодические тренировки, '
                                        'командные игры на выходных)',
                                        'Высокий уровень активности (тренировки 5+ часов в неделю, активные форматы '
                                        'отдыха, или тяжелый физический труд)',
                                        StateUserProfileTrain.question_volume_every_day_activity],
    question_sport_background=['Опишите Ваше спортивное прошлое',
                               'Опыта занятий спортом или соревнований нет',
                               'Есть опыт занятий спортом в детстве с участием в соревнованиях',
                               'Есть опыт занятий несколькими видами спорта от 2 лет и более с участием в '
                               'соревнованиях', StateUserProfileTrain.question_sport_background],
    question_volume_training=['Как Вы оцениваете свой уровень тренированности?',
                              'Начальный (техникой движений не владею, тренировки пугают)',
                              'Ниже среднего (владею техникой базовых движений, но не понимаю, если допускаю ошибки, '
                              'нужен контроль тренера)',
                              'Средний (уверенно владею техникой базовых движений, для выявления и работы над слабыми '
                              'местами нужен контроль тренера)',
                              'Выше среднего (уверенно владею техникой различных движений, умею самостоятельно '
                              'выявлять и корректировать слабые места)',
                              'Продвинутый (уверенно владею необходимыми мне двигательными навыками; знаю и работаю '
                              'над своими слабыми местами)', StateUserProfileTrain.question_volume_training],
    question_skills=['Какими навыками вы хотите овладеть?', StateUserProfileTrain.question_skills],
    question_meals=['Сколько в день приемов пищи у Вас обычно?', StateUserProfileTrain.question_meals],
    question_system_meals=['Придерживаетесь ли Вы какой либо системы питания? Если Вашей системы питания нету в списке,'
                           'опишите ее в сообщении',
                           'Веганство',
                           'Вегетарианство',
                           'Кето',
                           'Карнивор',
                           'Нет', StateUserProfileTrain.question_system_meals],
    question_alcohol=['Употребляете ли Вы алкоголь?',
                      'Да, 3-4 раза в неделю',
                      'Да, 1-2 раза в неделю',
                      'Только по праздникам',
                      'Да, 1-2 раза в месяц',
                      'Не употребляю совсем', StateUserProfileTrain.question_alcohol],
    question_vitamins=['Принимаете витамины или БАД? Какие? В какой дозировке?',
                       StateUserProfileTrain.question_vitamins],
)

the_limits_factors = dict(
    question_volume_stress=['Как Вы оцениваете уровень стресса в жизни?', [1, 10],
                            StateUserProfileLimitsFactors.question_volume_stress],
    question_quality_food=['Как Вы оцениваете качество питания?', [1, 10],
                           StateUserProfileLimitsFactors.question_quality_food],
    question_quality_sleep=['Как Вы оцениваете качество сна?', [1, 10],
                            StateUserProfileLimitsFactors.question_quality_sleep]
)

account_basic_data = dict(
    basic_data_menu=dict(
        name='Имя',
        surname='Фамилия',
        patronymic='Отчество',
        date_birth='Дата рождения',
        gender='Пол',
        height='Рост',
        weight='Вес',
        email='Email',
        phone='Телефон',
        comunication_channel='Канал связи'
    ),
    basic_data_states=dict(
        name=UserProfileBasicData.name,
        surname=UserProfileBasicData.surname,
        patronymic=UserProfileBasicData.patronymic,
        date_birth= UserProfileBasicData.date_birth,
        gender=UserProfileBasicData.gender,
        height=UserProfileBasicData.height,
        weight=UserProfileBasicData.weight,
        email=UserProfileBasicData.email,
        phone=UserProfileBasicData.phone,
        comunication_channel=UserProfileBasicData.communication_channels
    ),
    basic_data_update = dict(
        name='Введите ваше имя.',
        surname='Введите вашу фамилию.',
        patronymic='Ваше отчество, если нету оставьте поле пустым.',
        date_birth='Введите дату рождения в формате ДД.ММ.ГГГГ или ДД/ММ/ГГГГ.',
        gender = 'Выберите ваш пол.',
        height='Рост в сантиметрах',
        weight='Вес в килограммах',
        email='Введите email.',
        phone='Поделитесь своим контактом или введите номер телефона вручную.',
        comunication_channel='Выберите предпочтительный канал связи.'
    ),
    basic_data_link_datas = dict(
        name=Us.name,
        surname=StateUserProfileBasicData.surname,
        patronymic=StateUserProfileBasicData.patronymic,
        date_birth= StateUserProfileBasicData.date_birth,
        gender=StateUserProfileBasicData.gender,
        height=StateUserProfileBasicData.height,
        weight=StateUserProfileBasicData.weight,
        email=StateUserProfileBasicData.email,
        phone=StateUserProfileBasicData.phone,
        comunication_channel=StateUserProfileBasicData.communication_channels
    ),
    err_basic_data_update = dict(
        name = 'Ошибка. Для имени можно использовать любой набор символов менее 64 букв.'
                          + '\nЕсли вы считаете что ошибки нету, просим написать администратору в личку.',
        date_birth = 'Ошибка. Дата рождения в формате ДД.ММ.ГГГГ или ДД/ММ/ГГГГ.'
                                + '\nЕсли вы считаете что ошибки нету, просим написать администратору в личку.',
        gender = ('Ошибка. Для выбора пола воспользуйтесь кнопками ниже, или введите: '
                             '\n"men" - мужской, '
                             '\n"woman" - женский'
                             + '\nЕсли вы считаете что ошибки нету, просим написать администратору в личку.'
                             ),
        height = 'Ошибка. Укажите рост в сантиметрах.'
                            + '\nЕсли вы считаете что ошибки нету, просим написать администратору в личку.',
        weight = 'Ошибка. Укажите вес в килограммах.'
                            + '\nЕсли вы считаете что ошибки нету, просим написать администратору в личку.',
        email = 'Ошибка. Формат адреса электронной почты user@host.domain' + '\nЕсли вы считаете что ошибки нету, просим написать администратору в личку.',
        phone = 'Ошибка. Некорректный номер телефона'
                           + '\nЕсли вы считаете что ошибки нету, просим написать администратору в личку.',
        communication_channels = ('Ошибка. Для выбора пола воспользуйтесь кнопками ниже, или введите: '
                                             '\n"telegram" - Telegram'
                                             '\n"discord" - Дискорд'
                                             '\n"email" - Почта'
                                             '\n"phone" - Мобильная связь'
                                             + '\nЕсли вы считаете что ошибки нету, просим написать администратору в личку.'
                                             )
    ),
    account_menu_1='Ваш профиль.',
    account_menu_2='Для изменения нажмите на соответствующую кнопку.',
    account_qst_clear='У вас уже есть профиль, хотите его очистить?',
    account_rec_datas='Подождите, данные записываются.',
    clear_account_question='Хотите сбросить профиль?',
    clear_account_true='Аккаунт очищен.',
    clear_account_wait='Идет удаление аккаунта...',
    clear_account_cancel='Очистка аккаунта отменена.',
    update_profile_wait='Идет обновление данных...',
    update_account_true='Обновление данных прошло успешно.',
    update_account_false='При обновлении данных произошла ошибка.',
    update_profile_enter_data='Введите новые данные.',
)

question_for_profile = dict(
    the_basic_data=[
        'Основные данные', 'Данные для связи и т.д.(надо что-нить написать)',
        StateUserProfile.the_basic_data],
    the_questionnaire_questions=[
        'Физиология', 'Опросник по физиологической готовности к тренировкам PAR-Q',
        'Положительное действие двигательной активности на здоровье человека неоспоримо. Большинству '
        'людей следует регулярно тренироваться. Двигательная активность является безопасной для '
        'БОЛЬШИНСТВА людей. Опросник позволит понять, можно ли приступать к тренировкам или следует '
        'пройти дополнительное медицинское обследование перед тем, как начинать тренироваться.',
        StateUserProfile.the_questionnaire_questions],
    the_goals_questions=[
        'Цели', 'Какой-нить текст про цели, аналогичный "физиологии"(можно вставить картинки, '
                'гифки и др штуковины)',
        StateUserProfile.the_goals_questions],
    the_trane_questions=[
        'Тренировочный опыт', 'Такая же фигня про тренинги, как и про цели, но про тренинги.',
        StateUserProfile.the_trane_questions],
    the_limits_factors=[
        'Лимитирующие факторы', 'Такая же фигня',
        StateUserProfile.the_limits_factors]
)

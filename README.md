# Telegram-бот для тестов
В данный момент телеграмм бот используется для итоговой работы.

<img src="data/images/png" alt="drawing" width="200"/>


## Общие сведения.
Работает в асинхронном режиме с помощью библиотеки *asyncio*.

Я использовал библиотеку *aiogram* как основную для работы бота.
Бот взаимодействует через конечные автоматы.
Ради освоения материала, интерфейс был реализован посредством разных видов клавиатур:
1. **InlineKeyboard** - Для главного меню и меню профиля. Именно в ней я реализовал все колбэки.
2. **ReplyKeyboard** - Для прогноза погоды и всплывающих сообщений.
Клавиатура динамическая. Количество кнопок и текст меняется в зависимости от данных профиля.
Чтобы закрывать ReplyKeyboard при вызове InlineKeyboard, пришлось писать костыли. Можно было переписать все под один вид
клавиатуры или еще, что-нибудь придумать, но я не стал.


### О работе бота
#### Хранит у себя данные пользователя.
По средствам библиотеки PeeWee бот формирует базу данных пользователей SQLite.
Пользователи могут менять о себе любую информацию, кроме:
1. id (выдается автоматически)
2. user_id - id Telegram
3. is_active - активность юзера решил не прикручивать.

У пользователя есть право очистить свой профиль.

#### Показывает данные о прогнозе погоды.
В прогнозе погоды интерфейс реализовал в ReplyKeyboardMurkup


Данные берутся из [API OpenWeather.](https://openweathermap.org/api)
Бот дает в автоматическом режиме при входе в меню погоды прогноз на сегодня в выбранном городе.
Можно посмотреть прогноз на завтра на утро, день, вечер.
При первом запуске спрашивает местонахождение или название города.
Может хранить 6 избранных городов помимо выбранного. 

### Команды выполняемые ботом.
#### Везде
| Команда                                | Описание                                                                                        |
|----------------------------------------|-------------------------------------------------------------------------------------------------|
| /start	                                | Запуск бота. Автоматически создается аккаунт. При повторном вызове предлагает сбросить профиль. |
| /main_menu, Главное меню, Выйти в меню | Вывод главного меню.                                                                            |
| /weather_menu                          | Вывод меню прогноза погоды.                                                                     |
| /help	                                 | Список команд                                                                                   |
| /info	                                 | Вызов чата со службой поддержки.                                                                |
| /hello-world, Привет	                  | Приветствие.                                                                                    |
| Назад	                                 | Возвращает в предыдущее меню.                                                                   |


#### Прогноз погоды
| Команда                                        | Описание                                                                       |
|------------------------------------------------|--------------------------------------------------------------------------------|
| Погода на день	                                | Прогноз погоды на данное время                                                 |
| Погода на завтра                               | Погода на завтра в трех временных точках: 9, 15 и 21 час                       |
| Избранные города                               | Список избранных городов. Максимум 6.                                          |
| Выберите город или название выбранного города	 | Запрашивает у пользователя географическое положения для прогнозирования погоды |
| Поделиться геолокацией	                        | В режиме выбора города запрашивает у пользователя данные о местоположении.     |
| Добавить активный город                        | В режиме избранных городов добавляет активный город в список избранных         |
| Удалить из списка                              | В режиме избранных городов удаляет город из списка избранных.                  |



### Особенности
У вас должны быть установлены [зависимости проекта](requirements.txt)

1. Имя токена BOT_TOKEN.
2. Токен должен лежать => ./config/.env.
3. Cостояния пользователя держатся в оперативной памяти компьютера, поэтому после перезагрузки вся информация будет утеряна. 
Для постоянного хранения используйте базы данных.
4. Включена HTML разметка.
5. Включено игнорирование обработки сообщений если бот был выключен.
6. Включен Router для хранения кода в разных директориях и файлах, чтобы легче было его поддерживать.



## Зависимости
Эта программа зависит от интерпретатора Python версии 3.7 или выше.


## Структура проекта

### tele_bot
| Директория/файл                    | Описание                                                            |
|------------------------------------|---------------------------------------------------------------------|
| [callbacks](#callbacks)	           | Колбэки. Это реакции бота на нажатии кнопок в интерфейсе.           |
| [config](#config)                  | Все, что связано с путями на сторонние ресурсы, ключами и токенами. |
| [data](#data)                      | Файлы и данные. Все БД и все, что с ними связано .                  |
| [handlers](#handlers)	             | Обработчики. Реакции бота на сообщения и команды.                   |
| [keyboards](#keyboards)	           | Клавиатуры, кнопки.                                                 |
| [state_commands](#state_commands)	 | Обработчики состояний пользователя.                                 |
| [states](#states)	                 | Состояния пользователя.                                             |
| [utils](#utils)                    | Функциональность бота                                               |
| bot_main.py                        | Загрузочный файл                                                    |


### callbacks
| Директория/файл      | Описание                                 |
|----------------------|------------------------------------------|
| menu_other_call.py   | Колбэки главного меню.                   |
| user_account_call.py | Колбэки интерфейса профиля пользователя. |
| weather_call .py     | Колбэки интерфейса прогноза погоды.      |


### config
| Директория/файл | Описание                                                                                                                 |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| .env            | В данном файле должны лежать все ключи и токены для безопасности                                                         |
| config.py       | Для хранения всех url-ссылок сторонних ресурсов и переменные окружения, к которым можно обратиться за ключами и токенами |

### data
| Директория/файл | Описание                           |
|-----------------|------------------------------------|
| db_funcs.py     | Функции для работы с базой данных. |
| models.py       | Модели объектов БД.                |
| text.py         | Все текстовые ответы бота.         |

### handlers
| Директория/файл | Описание               |
|-----------------|------------------------|
| commands.py     | Обработчики команд.    |
| messages.py     | Обработчики сообщений. |

### keyboards
| Директория/файл    | Описание                          |
|--------------------|-----------------------------------|
| kb_user_profile.py | Главное меню и меню пользователя. |
| kb_weather.py      | Меню прогноза погоды.             |

### state_commands
| Директория/файл        | Описание                                    |
|------------------------|---------------------------------------------|
| menu_other_states.py   | Обработчик состояния главного меню.         |
| user_account_states.py | Обработчики состояний профиля пользователя. |
| weather_states.py      | Обработчики состояний прогноза погоды.      |

### states
| Директория/файл | Описание                           |
|-----------------|------------------------------------|
| states.py       | Состояния пользователя.            |

### utils
| Директория/файл | Описание                                                                |
|-----------------|-------------------------------------------------------------------------|
| easy_funcs.py   | Небольшие функции для обработки данных.                                 |
| weather.py      | Функции для работы с [API OpenWeather.](https://openweathermap.org/api) |


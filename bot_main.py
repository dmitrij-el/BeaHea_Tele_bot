"""
Телеграм бот работает в асинхронном режиме.
Имя токена BOT_TOKEN
Токен должен лежать ---> ./config/.env
База данных -----> ./data/beahea_bot.db
Включена память состояний пользователя
Включена HTML разметка
Включено игнорирование обработки сообщений если бот был выключен
Включен Router

Dirs:
config - конфигурационные файлы
data - данные и методы работы с ними
handlers - обработка ботом сообщений, команд и колбэков
keyboards - клавиатуры и кнопки
state_commands - обработка ботом состояний пользователя
states - состояния пользователя
utils - работа с API и другой функционал бота

"""

import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram_sqlite_storage.sqlitestore import SQLStorage
from aiogram.utils.chat_action import ChatActionMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config.config import BOT_TOKEN
from handlers.user_handlers import user_the_questionnaire, user_the_body_parameters, user_the_basic_data, main_menu_handlers
from handlers.admin_handlers import admin_list_handlers, adm_main_menu_handlers
from handlers.admin_handlers.sending_messages import scheduler_args
from handlers.user_handlers.user_the_questionnaire import MenuQuestionnaireStateFilter, QuestionsStateFilter

from pay import paid_features


async def run_bot():
    try:
        bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

        dp = Dispatcher(storage=SQLStorage('./datas/fsm.db'))
        scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
        scheduler.start()
        dp.message.middleware(ChatActionMiddleware())

        dp.include_router(main_menu_handlers.router)
        dp.include_router(user_the_basic_data.router)
        dp.include_router(user_the_body_parameters.router)
        dp.include_router(user_the_questionnaire.router)

        dp.include_router(admin_list_handlers.router)
        dp.include_router(adm_main_menu_handlers.router)



        dp.message.register(main_menu_handlers.t_channel,
                            F.text.lower().in_({"телеграм канал", "телеграм-канал"}))
        dp.message.register(main_menu_handlers.t_channel,
                            Command('open_channel'))


        dp.message.register(main_menu_handlers.send_to_Elya,
                            F.text.lower().in_({"написать эле"}))
        dp.message.register(main_menu_handlers.send_to_Elya,
                            Command('send_to_Elya'))

        dp.message.register(main_menu_handlers.private_channel,
                            F.text.lower().in_({"частный канал"}))
        dp.message.register(main_menu_handlers.private_channel,
                            Command('private_channel'))

        dp.message.register(main_menu_handlers.marathon,
                            F.text.lower().in_({"марафон мечты"}))
        dp.message.register(main_menu_handlers.marathon,
                            Command('marathon'))

        dp.message.register(main_menu_handlers.profile,
                            F.text.lower().in_({"профиль"}))
        dp.message.register(main_menu_handlers.profile,
                            Command('profile'))

        dp.message.register(main_menu_handlers.send_help,
                            F.text.lower().in_({"помощь", "help"}))
        dp.message.register(main_menu_handlers.send_help,
                            Command('help'))
        # dp.message.register(user_questions.menu_questions, MenuQuestionsStateFilter())

        scheduler_args(bot, scheduler)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as exp:
        logging.error(f'Ошибка в run_bot: {exp}')



if __name__ == "__main__":
    create_models()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run_bot())

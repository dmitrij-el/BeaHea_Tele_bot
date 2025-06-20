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
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_sqlite_storage.sqlitestore import SQLStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from data import models_peewee, text_user_profile
from config.config import BOT_TOKEN
from handlers import commands, messages
from state_commands import menu_other_states, user_profile_basic_data, user_questions
from pay import paid_features


async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher(storage=SQLStorage("data/database.db"))
    dp.message.middleware(ChatActionMiddleware())

    dp.include_router(messages.router)
    dp.include_router(commands.router)

    dp.include_router(menu_other_states.router)
    dp.include_router(user_profile_basic_data.router)
    dp.include_router(user_questions.router)

    dp.include_router(paid_features.router)
    dp.message.register(paid_features.process_successful_payment, F.successful_payment)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    models_peewee.create_models()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

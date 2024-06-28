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

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from data import models_peewee, text_user_profile
from config.config import BOT_TOKEN, API_URL_OPEN_WEATHER_DAY
from handlers import commands, messages
from state_commands import menu_other_states, user_account_states


async def main():
    f = text_user_profile.question_for_profile
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(ChatActionMiddleware())

    dp.include_router(messages.router)
    dp.include_router(commands.router)

    dp.include_router(menu_other_states.router)
    dp.include_router(user_account_states.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    models_peewee.create_models()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

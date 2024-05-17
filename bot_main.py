import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from Tbot_beahea.data import models
from Tbot_beahea.config.config import BOT_TOKEN
from Tbot_beahea.handlers import commands, messages, admin
from Tbot_beahea.state_commands import menu_other, user_accounts
from Tbot_beahea.callbacks import menu_others, user_account


"""
Телеграм бот работает в асинхронном режиме.
Имя токена BOT_TOKEN
Токен должен лежать --->  ./config/.env
База данных ----->   ./data/beahea_bot.db
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
async def main():


    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(ChatActionMiddleware())
    dp.include_router(commands.router)
    dp.include_router(menu_others.router)
    dp.include_router(user_account.router)
    dp.include_router(messages.router)
    dp.include_router(admin.router)
    dp.include_router(menu_other.router)
    dp.include_router(user_accounts.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    models.create_models()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
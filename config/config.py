"""
Конфигурационный файл для защиты ключей.
"""

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')
if BOT_TOKEN is None:
    exit('BOT_TOKEN отсутствует в переменных окружения')

TEST_PAYMENT_TOKEN_YOU_KASSA = os.getenv('TEST_PAYMENT_TOKEN_YOU_KASSA')
if TEST_PAYMENT_TOKEN_YOU_KASSA is None:
    exit('TEST_PAYMENT_TOKEN_YOU_KASSA отсутствует в переменных окружения')

TEST_PAYMENT_TOKEN_SBERBANK = os.getenv('TEST_PAYMENT_TOKEN_SBERBANK')
if TEST_PAYMENT_TOKEN_SBERBANK is None:
    exit('TEST_PAYMENT_TOKEN_SBERBANK отсутствует в переменных окружения')

ADMIN_DIMA = os.getenv('ADMIN_DIMA')
if ADMIN_DIMA is None:
    exit('ADMIN_DIMA отсутствует в переменных окружения')

DB_USER = os.getenv('DB_USER')
if ADMIN_DIMA is None:
    exit('DB_USER отсутствует в переменных окружения')

DB_PASSWORD = os.getenv('DB_PASSWORD')
if ADMIN_DIMA is None:
    exit('DB_PASSWORD отсутствует в переменных окружения')

DB_HOST = os.getenv('DB_HOST')
if DB_HOST is None:
    exit('DB_HOST отсутствует в переменных окружения')

DB_PORT = os.getenv('DB_PORT')
if DB_PORT is None:
    exit('DB_PORT отсутствует в переменных окружения')

DB_NAME = os.getenv('DB_NAME')
if DB_NAME is None:
    exit('DB_NAME отсутствует в переменных окружения')


class SettingsDataBase(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    # DATABASE_SQLITE = 'sqlite+aiosqlite:///data/db.sqlite3'

    def get_db_url(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")


settings = SettingsDataBase()
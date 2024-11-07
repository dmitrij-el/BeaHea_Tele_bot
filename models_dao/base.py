from functools import wraps
from typing import ClassVar, Type
from typing import Any
from uuid import UUID
from utils.logger import logger

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel, ValidationError


class BaseDAO:
    model = None  # Устанавливается в дочернем классе
    schemas_create: ClassVar[Type[BaseModel]] = None
    schemas_update: ClassVar[Type[BaseModel]] = None
    schemas_out: ClassVar[Type[BaseModel]] = None

    @staticmethod
    async def pre_add_check(db: AsyncSession, user_id: int, dict_values: dict[str, Any]):
        # Перехватчик на будущее, мало ли понадобится.
        pass

    @staticmethod
    def db_transaction_async(func):
        """
        Декоратор для обработки ошибок и отката транзакции.
        """

        @wraps(func)
        async def wrapper(db, user_id, *args, **kwargs):
            try:
                # Выполняем основную логику функции
                return await func(db, user_id, *args, **kwargs)
            except ValidationError as ve:
                # Логируем ошибку валидации данных Pydantic
                logger.error(f"Ошибка валидации данных: {ve}")
                raise
            except SQLAlchemyError as e:
                # Откатываем транзакцию при ошибке SQLAlchemy
                await db.rollback()
                logger.error(f"Ошибка базы данных: {e}")
                raise e

        return wrapper

    @classmethod
    @db_transaction_async
    async def get_cell_for_user_id(cls, db: AsyncSession, user_id: int, line_id: UUID):
        """
        Получение значения ячейки по id строки в таблице вызываемого дочернего класса для конкретного юзера.
        :param line_id: id строки.
        :param user_id: ID пользователя
        :param db: Асинхронная сессия I/O
        """
        name_table = cls.model.__name__.lower()
        logger.info(f"Получение {name_table} с ID: {line_id} для пользователя {user_id}")
        result = await db.execute(select(cls.model).where(cls.model.id == line_id, cls.model.user_id == user_id))
        result = result.first()
        if result:
            logger.info(f"{name_table.title()} с ID: {line_id} найдена для пользователя {user_id}")
        else:
            logger.warning(
                f"{name_table.title()} с ID: {line_id} не найдена или не принадлежит пользователю {user_id}")
        return result


    @classmethod
    @db_transaction_async
    async def get_line_for_user_id(cls, db: AsyncSession, user_id: int):
        """
        Получение значения всей строки в таблице вызываемого дочернего класса для конкретного юзера.
        :param user_id: ID пользователя
        :param db: Асинхронная сессия I/O

        """
        name_table = cls.model.__name__.lower()
        logger.info(f"Получение всех {name_table} для пользователя {user_id}")
        result = await db.execute(select(cls.model).where(cls.model.user_id == user_id))
        result = result.all()
        logger.info(f"Найдено {name_table}: {len(result)} для пользователя {user_id}")
        return result

    @classmethod
    @db_transaction_async
    async def add_one_entry_for_user_id(cls, db: AsyncSession, user_id: int, dict_values: dict[str, Any]):
        """
        Добавить одну запись в таблицу дочернего класса, используя Pydantic-схему для валидации
        :param dict_values:  Словарь с записью
        :param user_id: ID пользователя
        :param db: Асинхронная сессия I/O
        """

        dict_values['user_id'] = user_id
        name_table = cls.model.__name__.lower()
        # Используем Pydantic-схему для валидации
        validated_data = cls.schemas_create(**dict_values).dict()
        new_instance = cls.model(**validated_data)
        db.add(new_instance)
        await db.commit()
        await db.refresh(new_instance)
        logger.info(f"{name_table.title()} создана с ID: {new_instance.id} для пользователя {user_id}")
        return new_instance


    @classmethod
    @db_transaction_async
    async def add_many_entries_for_user_id(cls, db: AsyncSession, user_id: int, list_values: list[dict[str, Any]]):
        """
        Добавить несколько записей из списка list_values в таблицу дочернего класса с валидацией данных через Pydantic.
        :param list_values: Список словарей данных для создания записей
        :param user_id: ID пользователя
        :param db: Асинхронная сессия I/O
        """

        # В каждую запись добавляем user_id
        values_with_user_id = [{**values, "user_id": user_id} for values in list_values]
        # Валидация и создание экземпляров SQLAlchemy модели для каждого словаря в instances
        validated_values = [cls.schemas_create(**values).dict() for values in values_with_user_id]
        new_instances = [cls.model(**data) for data in validated_values]
        db.add_all(new_instances)
        await db.commit()
        return new_instances

    @classmethod
    @db_transaction_async
    async def update_cell_for_user_id(cls, db: AsyncSession, user_id: int, line_id: UUID, schema=schemas_update):
        """
        Обновление данных значения ячейки по id строки в таблице вызываемого
         дочернего класса для конкретного юзера с валидацией данных.
        :param line_id: id строки.
        :param user_id: ID пользователя
        :param db: Асинхронная сессия I/O
        :param schema: Модель для валидации данных

        """
        name_table = cls.model.__name__.lower()
        logger.info(f"Обновление категории с ID: {line_id} для пользователя {user_id}")
        db_category = await cls.get_cell_for_user_id(db, user_id, line_id)
        if db_category:
            for key, value in schema.dict(exclude_unset=True).items():
                setattr(db_category, key, value)
            await db.commit()
            await db.refresh(db_category)
            logger.info(f"{name_table.title()} с ID: {line_id} успешно обновлена для пользователя {user_id}")
        else:
            logger.warning(
                f"{name_table.title()} с ID: {line_id}"
                f" не найдена для обновления или не принадлежит пользователю {user_id}")
        return db_category

    @classmethod
    @db_transaction_async
    async def delete_cell_for_user_id(cls, db: AsyncSession, user_id: int, line_id: UUID):
        """
        Обновление данных значения ячейки по id строки в таблице вызываемого
         дочернего класса для конкретного юзера с валидацией данных.
        :param line_id: id строки.
        :param user_id: ID пользователя
        :param db: Асинхронная сессия I/O

        """
        name_table = cls.model.__name__.lower()
        logger.info(f'Удаление {name_table} с ID: {line_id} для пользователя {user_id}')
        db_collection = cls.get_cell_for_user_id(db, user_id, line_id)
        if db_collection:
            await db.delete(db_collection)
            await db.commit()
            logger.info(f'{name_table.title()} с ID: {line_id} успешно удалена для пользователя {user_id}.')
        else:
            logger.warning(
                f'{name_table.title()} с ID: {line_id}'
                f' не найдена для удаления или не принадлежит пользователю {user_id}.')
        return db_collection

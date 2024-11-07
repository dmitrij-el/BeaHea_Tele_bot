from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .base import BaseDAO
from models_sqlalchemy.model_user import User, Admin, UserBodyParameters, UserBasicData, UserProfileGoals, \
    UserProfileTrain, UserProfileLimitsFactors, UserProfileQuestionnaireQuestions



class UserDAO(BaseDAO):
    model = User


    @classmethod
    @BaseDAO.db_transaction_async
    async def add_user_with_reg(cls, db: AsyncSession, user_data: dict) -> User:
        """
        Добавляет пользователя и привязанный к нему основные данные.

        Аргументы:
        - session: AsyncSession - асинхронная сессия базы данных
        - user_data: dict - словарь с данными пользователя и профиля

        Возвращает:
        - User - объект пользователя
        """

        user = cls.model(
            user_id=user_data['user_id'],
            username=user_data['username']
        )
        db.add(user)
        await db.flush()

        profile = UserBasicData(
            name=user_data['name'],
            surname=user_data.get('surname')
        )
        db.add(profile)
        await db.commit()

        return user  # Возвращаем объект пользователя

    @classmethod
    async def get_user(cls, db: AsyncSession, user_id):
        result = await db.execute(select(cls.model).where(cls.model.id == user_id))
        return result.scalar_one_or_none()


    @classmethod
    async def get_username(cls, db: AsyncSession, user_id):
        # Создаем запрос для выборки username конкретного пользователя по его id
        query = select(cls.model.username).where(cls.model.id == user_id)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, db: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await db.execute(query)
        record = result.scalar_one_or_none()
        return record


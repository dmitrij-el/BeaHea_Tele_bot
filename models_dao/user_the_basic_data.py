from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .base import BaseDAO
from models_sqlalchemy.model_user import User, Admin, UserBodyParameters, UserBasicData, UserProfileGoals, \
    UserProfileTrain, UserProfileLimitsFactors, UserProfileQuestionnaireQuestions



class UserBasicDataDAO(BaseDAO):
    model = UserBasicData

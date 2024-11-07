from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .base import BaseDAO
from models_sqlalchemy.model_user import User, Admin, UserBodyParameters, UserBasicData, UserProfileGoals, \
    UserProfileTrain, UserProfileLimitsFactors, UserProfileQuestionnaireQuestions



class UserProfileQuestionnaireQuestionsDAO(BaseDAO):
    model = UserProfileQuestionnaireQuestions


class UserProfileGoalsDAO(BaseDAO):
    model = UserProfileGoals


class UserProfileTrainDAO(BaseDAO):
    model = UserProfileTrain


class UserProfileLimitsFactorsDAO(BaseDAO):
    model = UserProfileLimitsFactors

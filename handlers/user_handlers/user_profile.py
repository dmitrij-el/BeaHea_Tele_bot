"""
Сборник реакций на сообщения пользователя в состояниях относящихся к аккаунту
"""
from logging import Filter
from typing import Any

from aiogram import Router, Bot
from aiogram import flags
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from datas.models import models_user_questions, User
from keyboards.kb_user import kb_user_profile, kb_the_questionnaire
from datas.texts import text, text_user_questions
from handlers.required import user_required
from states.states import StateMenu, StateUserProfile, StateUserQuestionnaire, StateRedactorQuestionnaire
from states.states import StateUserProfileQuestionnaireQuestions, StateUserProfileGoals, StateUserProfileTrain, \
    StateUserProfileLimitsFactors
from states import states as st

router = Router()



"""
Сборник реакций на сообщения пользователя в состояниях относящихся к аккаунту
"""
from aiogram import Router, Bot
from aiogram import flags
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Filter

from handlers.required import user_required
from datas.texts import text, text_account_basic_datas
from datas.models.models_setting import User, Gender
from keyboards import kb_main_menu
from keyboards.kb_user import kb_user_profile
from states.states import (StateMenu,
                           StateUserProfile,
                           StateUserProfileBasicData)
from utils import easy_funcs

router = Router()
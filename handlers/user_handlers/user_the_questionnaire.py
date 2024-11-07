"""
Сборник реакций на сообщения пользователя в состояниях относящихся к аккаунту
"""
from logging import Filter
from typing import Any

from aiogram import Router, Bot
from aiogram import flags
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from datas.models.models_user import User
from keyboards.kb_user import kb_user_profile, kb_the_questionnaire
from datas.texts import text, text_user_questions
from handlers.required import user_required
from states.states import StateMenu, StateUserProfile, StateUserQuestionnaire, StateRedactorQuestionnaire
from states.states import StateUserProfileQuestionnaireQuestions, StateUserProfileGoals, StateUserProfileTrain, \
    StateUserProfileLimitsFactors
from states import states as st

router = Router()


async def get_class_str(state: FSMContext) -> Any:
    # Получает название текущего класса группы состояния
    current_state = await state.get_state()
    if current_state is not None:
        group_name, _ = current_state.split(':')
        return group_name


async def get_state_str(state: FSMContext) -> Any:
    # Получает название конкретного состояния внутри группы
    current_state = await state.get_state()
    if current_state is not None:
        _, state_name = current_state.split(':')
        return state_name


@router.message(StateUserProfile.the_questionnaire)
@user_required
async def user_profile(msg: Message, state: FSMContext, bot: Bot):
    print('Я в the_questionnaire')
    prompt = msg.text
    for key, value in text_user_questions.user_profile.items():
        if prompt == value[0]:
            next_state = getattr(StateUserQuestionnaire, key)
            text_mess = value[1]
            kb = kb_the_questionnaire.user_menu_question_for_profile
            await state.set_state(next_state)
            await msg.answer(text=text_mess, reply_markup=kb(user_id=msg.from_user.id))


class MenuQuestionnaireStateFilter(Filter):
    async def __call__(self, message: Message, state: FSMContext) -> bool:
        now_state = await state.get_state()
        if now_state in [
            StateUserQuestionnaire.the_questionnaire_questions,
            StateUserQuestionnaire.the_goals_questions,
            StateUserQuestionnaire.the_trane_questions,
            StateUserQuestionnaire.the_limits_factors
        ]:
            return True


class QuestionsStateFilter(Filter):
    async def __call__(self, message: Message, state: FSMContext) -> bool:
        print('Я в QuestionsStateFilter')

        now_state = await state.get_state()
        # Разбиваем состояние на главное и дочернее
        name_class_now = await get_class_str(state=state)
        name_state_now = await get_state_str(state=state)
        # Перебираем словарь состояний и ищем совпадения по первым ключам.
        # Это для всех вопросов в меню профиля пользователя. АНкетЫ
        the_questions = text_user_questions.the_questionnaire
        for key_par_status, ch_status in the_questions.items():
            for main_state, states_list in ch_status.items():
                for st in states_list:
                    if st == states_list:
                        return True

#
# @router.message(MenuQuestionnaireStateFilter())
# @user_required
# @flags.chat_action("typing")
# async def the_questionnaire(msg: Message, state: FSMContext, bot: Bot):
#     prompt = msg.text
#     user_id = msg.from_user.id
#     user = User.get_user_by_id(user_id=user_id)
#
#     user_questionnaire = user.the_questionnaire  # Получаем объект UserQuestionnaire, связанный с пользователем
#     name_class_now = await get_class_str(state=state)  # Имя класса состояния StateUserQuestionnaire
#     name_state_now = await get_state_str(state=state)  # Имя состояния the_questionnaire_questions
#
#     name_class_base = name_class_now.replace('State', '', 1)  # Имя класса модели UserQuestionnaire
#     name_base = name_state_now  # Имя параметра модели the_questionnaire_questions
#
#     # Проверяем, есть ли связанные данные в UserProfileQuestionnaire
#     section_data = getattr(user_questionnaire, name_base, None)
#     if section_data:
#         # Пройтись по всем полям внутри UserProfileQuestionnaireQuestions
#         for field in section_data._meta.sorted_fields:
#             value = getattr(section_data, field.name, None)
#             if value is None:
#                 # допустим field == question_diagnosis_fainting. Может такое быть?
#                 name_class_model = field.model.__name__
#                 name_class_state = 'State' + name_class_model  # Имя класса состояния StateProfileQuestionnaireQuestions
#                 class_state = getattr(st, name_class_state)  # Получили класс состояния
#                 next_state = getattr(class_state,
#                                      field)  # Получили состояние StateProfileQuestionnaireQuestions.question_diagnosis_fainting если field == question_diagnosis_fainting
#                 dict_questions = getattr(text_user_questions, name_state_now)
#                 text = dict_questions[field]
#                 kb = kb_the_questionnaire.user_question(user_id=user_id)
#                 await state.set_state(next_state)
#                 await msg.answer(text=text, reply_markup=kb)
#         else:
#             next_state = getattr(StateUserQuestionnaire, name_state_now)
#             text = text_user_questions.the_questionnaire[name_state_now][1]
#             kb = kb_user_profile.the_questionnaire(user_id=user_id)
#             print("Все поля заполнены в UserProfileQuestionnaire.")
#     else:
#         name_class_state = next(iter(text_user_questions.the_questionnaire_states[name_state_now]))
#         class_state = getattr(st, name_class_state)
#         next_name_state = text_user_questions.the_questionnaire_states[name_state_now][name_class_state][0]
#         next_state = getattr(class_state, next_name_state)
#         text = text_user_questions.the_questionnaire[name_state_now][1]
#         kb = kb_the_questionnaire.user_question(user_id=user_id)
#         print("Нет данных в UserProfileQuestionnaire.")
#     await state.set_state(next_state)
#     await msg.answer(text=text, reply_markup=kb)


@router.message(QuestionsStateFilter())
@user_required
@flags.chat_action("typing")
async def questions(msg: Message, state: FSMContext, bot: Bot):
    pass



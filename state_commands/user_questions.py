"""
Сборник реакций на сообщения пользователя в состояниях относящихся к аккаунту
"""
from aiogram import Router
from aiogram import flags
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards import kb_user_questions, kb_user_profile, kb_main_menu
from data import text, text_user_profile
from states.states import (StateMenu,
                           StateUserProfile,
                           StateUserProfileBasicData,
                           StateUserProfileQuestionnaire,
                           StateUserProfileGoals,
                           StateUserProfileTrain)

router = Router()

list_the_questionnaire_questions = ['question_number_of_meals',
                                    'question_diagnosis_high_low_pressure',
                                    'question_diagnosis_chronic_disease',
                                    'question_diagnosis_fainting',
                                    'question_problem_musculoskeletal_system',
                                    'question_physical_activity_restrictions',
                                    'question_taking_medications',
                                    'question_injuries_with_intervention']

list_the_goals_questions = ['question_list_of_goals',
                            'question_one_goal_from_list',
                            'question_formulate_goal',
                            'question_reasons_goal',
                            'question_actions_to_achieve_the_goal',
                            'question_obstacles_on_the_way',
                            'question_help_to_the_goal',
                            'question_weight_5_year']

list_the_trane_questions = ['question_exp_weight_training',
                            'question_regularly_train_at_the_moment',
                            'question_volume_every_day_activity',
                            'question_sport_background',
                            'question_volume_training',
                            'question_skills',
                            'question_meals',
                            'question_system_meals',
                            'question_alcohol',
                            'question_vitamins']

list_the_limits_factors = ['question_volume_stress',
                           'question_quality_food',
                           'question_quality_sleep']


@router.message(StateUserProfileQuestionnaire.question_number_of_meals)
@flags.chat_action("typing")
async def profile(msg: Message, state: FSMContext):
    if state.get_state() is StateUserProfileQuestionnaire.question_number_of_meals:
        prompt = msg.text
        await msg.answer(text=text_user_profile.question_for_profile)
    current_state = await state.get_state()
    current_state_str = current_state.split(':')[-1]
    current_index = list_the_questionnaire_questions.index(current_state_str)


@router.message(StateUserProfileGoals.question_reasons_goal)
@flags.chat_action("typing")
async def profile(msg: Message, state: FSMContext):
    prompt = msg.text
    current_state = await state.get_state()
    current_state_str = current_state.split(':')[-1]
    current_index = list_the_questionnaire_questions.index(current_state_str)
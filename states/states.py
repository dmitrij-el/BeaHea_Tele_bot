from aiogram.fsm.state import StatesGroup, State

"""
Стадии взаимодействия с ботом.

"""


class StateMenu(StatesGroup):
    menu = State()
    telegram_channel = State()
    profile = State()


class StateUserProfile(StatesGroup):
    the_basic_data = State()
    the_questionnaire_questions = State()
    the_goals_questions = State()
    the_trane_questions = State()
    the_limits_factors = State()


class StateUserProfileBasicData(StatesGroup):
    change_name = State()
    change_surname = State()
    change_patronymic = State()
    change_date_birth = State()
    change_gender = State()
    change_height = State()
    change_weight = State()
    change_email = State()
    change_phone = State()
    change_communication_channels = State()
    clear_profile = State()


class StateUserProfileQuestionnaire(StatesGroup):
    question_number_of_meals = State()
    question_diagnosis_high_low_pressure = State()
    question_diagnosis_chronic_disease = State()
    question_diagnosis_fainting = State()
    question_problem_musculoskeletal_system = State()
    question_physical_activity_restrictions = State()
    question_taking_medications = State()
    question_injuries_with_intervention = State()


class StateUserProfileGoals(StatesGroup):
    question_list_of_goals = State()
    question_one_goal_from_list = State()
    question_formulate_goal = State()
    question_reasons_goal = State()
    question_actions_to_achieve_the_goal = State()
    question_obstacles_on_the_way = State()
    question_help_to_the_goal = State()
    question_weight_5_year = State()


class StateUserProfileTrain(StatesGroup):
    question_exp_weight_training = State()
    question_regularly_train_at_the_moment = State()
    question_volume_every_day_activity = State()
    question_sport_background = State()
    question_volume_training = State()
    question_skills = State()
    question_meals = State()
    question_system_meals = State()
    question_alcohol = State()
    question_vitamins = State()


class StateUserProfileLimitsFactors(StatesGroup):
    question_volume_stress = State()
    question_quality_food = State()
    question_quality_sleep = State()

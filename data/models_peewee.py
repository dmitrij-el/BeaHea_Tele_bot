import datetime
import logging

from peewee import (CharField, DateTimeField, SqliteDatabase, DateField,
                    IntegerField, BooleanField, ForeignKeyField)
from peewee import Model, InternalError, PrimaryKeyField


def create_models() -> None:
    """
    Создание БД
    :return: None
    """
    try:
        data_gender = [
            {'name': 'men', 'symbol': '♂️'},
            {'name': 'women', 'symbol': '♀️'}
        ]
        data_channels = [
            {'name': 'Telegram'},
            {'name': 'Whatsapp'},
            {'name': 'Viber'},
            {'name': 'Телефон', 'symbol': '📞'}
        ]
        data_video_channels = [
            {'name': 'Telegram'},
            {'name': 'Whatsapp'},
            {'name': 'GoogleMeet'}
        ]

        Gender.create_table()
        User.create_table()
        ChannelCom.create_table()
        VideoChannelCom.create_table()
        UserProfileBasicData.create_table()
        UserProfileQuestionnaire.create_table()
        UserProfileTrain.create_table()
        UserProfileGoals.create_table()
        UserProfileLimitsFactors.create_table()

        with db_beahea.atomic():
            for gender in Gender.select():
                gender.delete_instance()
            for channel in ChannelCom.select():
                channel.delete_instance()
            for video_channel in VideoChannelCom.select():
                video_channel.delete_instance()
            for data_dict in data_gender:
                Gender.create(**data_dict)
            for data_dict in data_channels:
                ChannelCom.create(**data_dict)
            for data_dict in data_video_channels:
                VideoChannelCom.create(**data_dict)
    except InternalError as pw:
        logging.error(pw)


db_beahea = SqliteDatabase('./data/database.db')


class BaseUserModel(Model):
    class Meta:
        database = db_beahea
        order_by = 'id'


class Gender(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    name = CharField(unique=True)
    symbol = CharField(unique=True)

    class Meta:
        db_table = "gender"


class ChannelCom(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    name = CharField(unique=True)
    symbol = CharField(null=True)

    class Meta:
        db_table = "channel_com"


class VideoChannelCom(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    name = CharField(unique=True)
    symbol = CharField(null=True)

    class Meta:
        db_table = "video_channel_com"


class User(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    creation_time = DateTimeField(default=datetime.datetime.now)
    is_active = BooleanField(default=True)
    user_id = CharField(unique=True)
    state_now = CharField(null=True)



    class Meta:
        db_table = "user"


class UserProfileBasicData(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    user_id = ForeignKeyField(User, to_field='user_id')
    all_complicate = BooleanField(default=False)

    name = CharField(max_length=63, null=True)
    surname = CharField(max_length=63, null=True)
    username = CharField(null=True)
    patronymic = CharField(max_length=63, null=True)
    date_birth = DateField(null=True)
    gender = ForeignKeyField(Gender, backref='user', null=True)
    height = IntegerField(null=True)
    weight = IntegerField(null=True)
    phone = CharField(unique=True, index=True, null=True)
    email = CharField(unique=True, index=True, null=True)
    communication_channels = ForeignKeyField(ChannelCom, backref='user', null=True)

    class Meta:
        db_table = "basic_data"


class UserProfileQuestionnaire(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    user_id = ForeignKeyField(User, to_field='user_id')
    all_complicate = BooleanField(default=False)

    question_number_of_meals = CharField(null=True)
    question_diagnosis_high_low_pressure = BooleanField(null=True)
    question_diagnosis_chronic_disease = BooleanField(null=True)
    question_diagnosis_fainting = BooleanField(null=True)
    question_problem_musculoskeletal_system = BooleanField(null=True)
    question_physical_activity_restrictions = BooleanField(null=True)
    question_taking_medications = BooleanField(null=True)
    question_injuries_with_intervention = BooleanField(null=True)

    class Meta:
        db_table = "questionnaire_questions"


class UserProfileGoals(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    user_id = ForeignKeyField(User, to_field='user_id')
    all_complicate = BooleanField(default=False)

    question_list_of_goals = CharField(null=True)
    question_one_goal_from_list = CharField(null=True)
    question_formulate_goal = CharField(null=True)
    question_reasons_goal = CharField(null=True)
    question_actions_to_achieve_the_goal = CharField(null=True)
    question_obstacles_on_the_way = CharField(null=True)
    question_help_to_the_goal = CharField(null=True)
    question_weight_5_year = CharField(null=True)

    class Meta:
        db_table = "goals_questions"


class UserProfileTrain(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    user_id = ForeignKeyField(User, to_field='user_id')
    all_complicate = BooleanField(default=False)

    question_exp_weight_training = CharField(null=True)
    question_regularly_train_at_the_moment = CharField(null=True)
    question_volume_every_day_activity = CharField(null=True)
    question_sport_background = CharField(null=True)
    question_volume_training = CharField(null=True)
    question_skills = CharField(null=True)
    question_meals = CharField(null=True)
    question_system_meals = CharField(null=True)
    question_alcohol = CharField(null=True)
    question_vitamins = CharField(null=True)

    class Meta:
        db_table = "trane_questions"


class UserProfileLimitsFactors(BaseUserModel):
    id = PrimaryKeyField(unique=True)
    user_id = ForeignKeyField(User, to_field='user_id')
    all_complicate = BooleanField(default=False)

    question_volume_stress = CharField(null=True)
    question_quality_food = CharField(null=True)
    question_quality_sleep = CharField(null=True)

    class Meta:
        db_table = "limits_factors_questions"

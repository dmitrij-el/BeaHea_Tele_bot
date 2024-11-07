from sqlalchemy import ForeignKey, Date, text, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, uniq_str_an, uniq_int_an
from .user_profile import User
from ..enums_models import RangeFrom1To10


class UserProfileQuestionnaireQuestions(Base):
    the_questionnaire: Mapped[str | None]
    question_number_of_meals: Mapped[str | None]
    question_diagnosis_high_low_pressure: Mapped[str | None]
    question_diagnosis_chronic_disease: Mapped[str | None]
    question_diagnosis_fainting: Mapped[str | None]
    question_problem_musculoskeletal_system: Mapped[str | None]
    question_physical_activity_restrictions: Mapped[str | None]
    question_taking_medications: Mapped[str | None]
    question_injuries_with_intervention: Mapped[str | None]

    user: Mapped["User"] = relationship(
        "User",
        back_populates="the_questionnaire_questions",
        uselist=False
    )


class UserProfileGoals(Base):
    question_list_of_goals: Mapped[str | None]
    question_one_goal_from_list: Mapped[str | None]
    question_formulate_goal: Mapped[str | None]
    question_reasons_goal: Mapped[str | None]
    question_actions_to_achieve_the_goal: Mapped[str | None]
    question_obstacles_on_the_way: Mapped[str | None]
    question_help_to_the_goal: Mapped[str | None]
    question_weight_5_year: Mapped[str | None]

    user: Mapped["User"] = relationship(
        "User",
        back_populates="the_goals_questions",
        uselist=False
    )



class UserProfileTrain(Base):
    question_exp_weight_training: Mapped[str | None]
    question_regularly_train_at_the_moment: Mapped[str | None]
    question_volume_every_day_activity: Mapped[str | None]
    question_sport_background: Mapped[str | None]
    question_volume_training: Mapped[str | None]
    question_skills: Mapped[str | None]
    question_meals: Mapped[str | None]
    question_system_meals: Mapped[str | None]
    question_alcohol: Mapped[str | None]
    question_vitamins: Mapped[str | None]

    user: Mapped["User"] = relationship(
        "User",
        back_populates="the_trane_questions",
        uselist=False
    )

class UserProfileLimitsFactors(Base):
    question_volume_stress: Mapped[RangeFrom1To10 | None]
    question_quality_food: Mapped[RangeFrom1To10 | None]
    question_quality_sleep: Mapped[RangeFrom1To10 | None]

    user: Mapped["User"] = relationship(
        "User",
        back_populates="the_limits_factors",
        uselist=False
    )

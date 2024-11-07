from sqlalchemy import ForeignKey, Date, text, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, uniq_str_an, uniq_int_an
from .. import (UserBasicData, UserBodyParameters, UserProfileQuestionnaireQuestions,
                UserProfileGoals, UserProfileTrain, UserProfileLimitsFactors)


class User(Base):
    user_id: Mapped[uniq_int_an]
    username: Mapped[uniq_str_an]
    is_active: Mapped[bool] = mapped_column(default=True)
    the_basic_data: Mapped['UserBasicData'] = relationship(
        back_populates='user',
        uselist=False,
        lazy="joined"
    )
    the_body_parameters: Mapped['UserBodyParameters'] = relationship(
        back_populates='user',
        cascade="all, delete-orphan"
    )
    the_questionnaire_questions: Mapped['UserProfileQuestionnaireQuestions'] = relationship(
        back_populates='user',
        uselist=False,
        lazy="joined"
    )
    the_goals_questions: Mapped['UserProfileGoals'] = relationship(
        back_populates='user',
        uselist=False,
        lazy="joined"
    )
    the_trane_questions: Mapped['UserProfileTrain'] = relationship(
        back_populates='user',
        uselist=False,
        lazy="joined"
    )
    the_limits_factors: Mapped['UserProfileLimitsFactors'] = relationship(
        back_populates='user',
        uselist=False,
        lazy="joined"
    )
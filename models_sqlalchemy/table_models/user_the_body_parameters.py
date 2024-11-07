from sqlalchemy import ForeignKey, Date, text, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, uniq_str_an, uniq_int_an
from .user_profile import User



class UserBodyParameters(Base):
    height: Mapped[DECIMAL[3, 0] | None]
    weight: Mapped[DECIMAL[3, 0] | None]
    breast_vol: Mapped[DECIMAL[5, 1] | None]
    waist_size: Mapped[DECIMAL[5, 1] | None]
    buttock_volume: Mapped[DECIMAL[5, 1] | None]
    hip_volume: Mapped[DECIMAL[5, 1] | None]
    shin_volume: Mapped[DECIMAL[5, 1] | None]
    shoulder_volume: Mapped[DECIMAL[5, 1] | None]
    shoulder_volume_in_stressed: Mapped[DECIMAL[5, 1] | None]
    user: Mapped["User"] = relationship(
        "User",
        back_populates="the_body_parameters",
        uselist=False
    )

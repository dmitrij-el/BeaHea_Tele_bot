from sqlalchemy import ForeignKey, Date, text, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, uniq_str_an, uniq_int_an
from .user_profile import User


class Admin(User):
    is_admin: Mapped[bool] = mapped_column(default=False)


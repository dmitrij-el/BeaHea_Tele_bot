from sqlalchemy import ForeignKey, Date, text, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, uniq_str_an, uniq_int_an
from ..enums_models import GenderEnum, VideoChannelComEnum, ChannelComEnum




class UserBasicData(Base):
    name: Mapped[str]
    surname: Mapped[str | None]
    patronymic: Mapped[str | None]
    date_birth: Mapped[Date | None]
    gender: Mapped[GenderEnum] = mapped_column(default=GenderEnum.GENDER, server_default=text("'GENDER'"))
    phone: Mapped[int | None]
    email: Mapped[uniq_str_an | None]
    communication_channels: Mapped[ChannelComEnum | None] = mapped_column(default=ChannelComEnum.CHANNEL,
                                                                          server_default=text("'CHANNEL'"))
    video_communication_channels: Mapped[VideoChannelComEnum | None] = mapped_column(default=VideoChannelComEnum.CHANNEL,
                                                                                     server_default=text("'VIDEO_CHANNEL'"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="the_basic_data",
        uselist=False
    )
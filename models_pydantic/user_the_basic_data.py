from typing import List
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Date

from models_sqlalchemy.enums_models import GenderEnum, VideoChannelComEnum, ChannelComEnum, RangeFrom1To10



class UserBasicDataPydantic(BaseModel):
    name: str
    surname: str | None
    patronymic: str | None
    date_birth: Date | None
    gender: GenderEnum
    phone: int | None
    email: str | None
    communication_channels: ChannelComEnum | None
    video_communication_channels: VideoChannelComEnum | None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
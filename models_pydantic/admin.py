from typing import List
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Date

from models_sqlalchemy.enums_models import GenderEnum, VideoChannelComEnum, ChannelComEnum, RangeFrom1To10

class AdminPydantic(BaseModel):
    is_admin: bool

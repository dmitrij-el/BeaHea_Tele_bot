from enum import StrEnum, IntEnum


class GenderEnum(StrEnum):
    GENDER = "пол"
    MALE = "мужчина"
    FEMALE = "женщина"


class ChannelComEnum(StrEnum):
    CHANNEL = 'Канал связи'
    TELEGRAM = 'Telegram'
    WHATSAPP = 'Whatsapp'
    VIBER = 'Viber'
    PHONE = 'Мобильный'


class VideoChannelComEnum(StrEnum):
    CHANNEL = 'Видео канал'
    TELEGRAM = 'Telegram'
    WHATSAPP = 'Whatsapp'
    GOOGLE = 'GoogleMeet'


class RangeFrom1To10(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10

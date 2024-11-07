from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from datas.texts import text_of_paid_service
from utils import easy_funcs
from states.states import StateMenu


def go_to_telegram_channel() -> InlineKeyboardMarkup:
    telegram_channel_buttons = [
        [InlineKeyboardButton(text='Эля, Еда и Гантеля.', url='t.me/beahea_public')]
    ]
    telegram_channel_keyboard = InlineKeyboardMarkup(inline_keyboard=telegram_channel_buttons)
    return telegram_channel_keyboard


def not_go_to_private_telegram_channel() -> InlineKeyboardMarkup:
    go_to_private_telegram_channel_buttons = [
        [InlineKeyboardButton(text='Купить подписку на частный канал',
                              callback_data='pay_subscription')]
    ]
    go_to_private_telegram_channel_keyboard = InlineKeyboardMarkup(
        inline_keyboard=go_to_private_telegram_channel_buttons)
    return go_to_private_telegram_channel_keyboard


def not_go_to_marathon_channel() -> InlineKeyboardMarkup:
    go_to_marathon_buttons = [
        [InlineKeyboardButton(text='Купить марафон мечты',
                              callback_data='pay_marathon')]
    ]
    go_to_marathon_keyboard = InlineKeyboardMarkup(inline_keyboard=go_to_marathon_buttons)
    return go_to_marathon_keyboard


def go_to_private_telegram_channel() -> InlineKeyboardMarkup:
    go_to_private_telegram_channel_buttons = [
        [InlineKeyboardButton(text=text_of_paid_service.subscribe_private_channel_paid_for,
                              url='t.me/+gviRTSrSnEs4ZjNi')]
    ]
    go_to_private_telegram_channel_keyboard = InlineKeyboardMarkup(
        inline_keyboard=go_to_private_telegram_channel_buttons)
    return go_to_private_telegram_channel_keyboard


def go_to_marathon_channel() -> InlineKeyboardMarkup:
    go_to_marathon_buttons = [
        [InlineKeyboardButton(text=text_of_paid_service.button_subscribe_marathon_paid_for,
                              url='t.me/+wWx0bowVOs41NWVi')]
    ]
    go_to_marathon_keyboard = InlineKeyboardMarkup(inline_keyboard=go_to_marathon_buttons)
    return go_to_marathon_keyboard

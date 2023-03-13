from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_admin import LEXICON_KEYBOARDS_ADMIN


def create_is_available_keyboard() -> ReplyKeyboardMarkup:
    available_button: KeyboardButton = KeyboardButton(text=LEXICON_KEYBOARDS_ADMIN['available_button'])
    not_available_button: KeyboardButton = KeyboardButton(text=LEXICON_KEYBOARDS_ADMIN['not_available_button'])
    availability_builder: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[available_button, not_available_button]],
                                                                    resize_keyboard=True)
    return availability_builder


def create_allow_publishing_keyboard() -> ReplyKeyboardMarkup:
    allow_publishing_button: KeyboardButton = KeyboardButton(text=LEXICON_KEYBOARDS_ADMIN['allow_publishing_button'])
    not_allow_publishing_button: KeyboardButton = KeyboardButton(
        text=LEXICON_KEYBOARDS_ADMIN['not_allow_publishing_button'])
    allow_publishing_builder: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[allow_publishing_button, not_allow_publishing_button]],
        resize_keyboard=True)
    return allow_publishing_builder

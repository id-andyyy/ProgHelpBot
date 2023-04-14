from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.admin_lexicon import LEXICON_KEYBOARDS_ADMIN
from database.sqlite import sql_get_sections


async def create_sections_keyboard() -> ReplyKeyboardMarkup:
    sections: list[tuple[int | str]] = await sql_get_sections()

    sections_builder: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=f'{section[1]}')] for section in sorted(sections, key=lambda x: x[2])],
        resize_keyboard=True)

    return sections_builder


async def create_is_published_keyboard() -> ReplyKeyboardMarkup:
    is_published_button: KeyboardButton = KeyboardButton(text=LEXICON_KEYBOARDS_ADMIN['is_published_button'])
    not_is_published_button: KeyboardButton = KeyboardButton(text=LEXICON_KEYBOARDS_ADMIN['not_is_published_button'])
    is_published_builder: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[is_published_button, not_is_published_button]],
        resize_keyboard=True)
    return is_published_builder


async def create_allow_publishing_keyboard() -> ReplyKeyboardMarkup:
    allow_publishing_button: KeyboardButton = KeyboardButton(text=LEXICON_KEYBOARDS_ADMIN['allow_publishing_button'])
    not_allow_publishing_button: KeyboardButton = KeyboardButton(
        text=LEXICON_KEYBOARDS_ADMIN['not_allow_publishing_button'])
    allow_publishing_builder: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[allow_publishing_button, not_allow_publishing_button]],
        resize_keyboard=True)
    return allow_publishing_builder

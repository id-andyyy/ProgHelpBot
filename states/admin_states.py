from aiogram.filters import StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage

storage: MemoryStorage = MemoryStorage()

user_dict: dict[int, dict[str, str | list | int | bool]] = {}


class FSMAddArticle(StatesGroup):
    fill_title = State()
    fill_emoji = State()
    fill_link = State()
    fill_keywords = State()
    fill_section = State()
    fill_position = State()
    fill_is_available = State()
    allow_publishing = State()

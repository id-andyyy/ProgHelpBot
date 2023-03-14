from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_data.config import load_config

config = load_config(r'.env')

admin_ids: list[int] = config.tg_bot.admin_ids


class IsAdmin(BaseFilter):
    def __init__(self) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat

from filters.is_admin import IsAdmin

from lexicon.lexicon_user import LEXICON_COMMANDS_USER
from lexicon.lexicon_admin import LEXICON_COMMANDS_ADMIN

from config_data.config import load_config

config = load_config(r'.env')

admin_ids: list[int] = config.tg_bot.admin_ids


async def set_user_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command, description in LEXICON_COMMANDS_USER.items()]

    await bot.set_my_commands(commands=main_menu_commands)


async def set_admin_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command, description in {**LEXICON_COMMANDS_USER, **LEXICON_COMMANDS_ADMIN}.items()]

    for admin_id in admin_ids:
        await bot.set_my_commands(commands=main_menu_commands, scope=BotCommandScopeChat(chat_id=admin_id))

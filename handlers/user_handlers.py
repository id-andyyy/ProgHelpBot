from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message

from lexicon.lexicon_user import LEXICON_USER

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_USER['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_USER['/help'])


@router.message(Command(commands=['creator']))
async def process_creator_command(message: Message):
    await message.answer(text=LEXICON_USER['/creator'])

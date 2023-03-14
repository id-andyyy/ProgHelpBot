from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message

from lexicon.lexicon_user import LEXICON_USER
from database.sqlite import sql_get_articles
from services.services import get_articles

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_USER['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_USER['/help'])


@router.message(Command(commands=['articles']))
async def process_articles_command(message: Message):
    await message.answer(text=await get_articles(), disable_web_page_preview=True)


@router.message(Command(commands=['creator']))
async def process_creator_command(message: Message):
    await message.answer(text=LEXICON_USER['/creator'])

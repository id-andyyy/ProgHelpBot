from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message

from lexicon.user_lexicon import LEXICON_USER
from services.services import print_articles, find_articles

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_USER['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_USER['/help'])


@router.message(Command(commands=['articles']))
async def process_articles_command(message: Message):
    await message.answer(text=await print_articles(), disable_web_page_preview=True)


@router.message(Command(commands=['search']))
async def process_search_command(message: Message):
    await message.answer(text=LEXICON_USER['/search'])


@router.message(Command(commands=['feedback']))
async def process_feedback_command(message: Message):
    await message.answer(text=LEXICON_USER['/feedback'])


@router.message(Command(commands=['creator']))
async def process_creator_command(message: Message):
    await message.answer(text=LEXICON_USER['/creator'])


@router.message()
async def process_search(message: Message):
    await message.answer(text=await print_articles(data=await find_articles(message.text), search_mode=True),
                         disable_web_page_preview=True)

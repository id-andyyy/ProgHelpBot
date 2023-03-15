from aiogram import F
from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, ReplyKeyboardRemove

from states.admin_states import *
from lexicon.lexicon_admin import LEXICON_ADMIN, LEXICON_KEYBOARDS_ADMIN
from filters.is_admin import IsAdmin
from keyboards.admin_keyboard import *
from database.sqlite import sql_add_article
from services.services import get_articles, print_articles, handle_article_data

router: Router = Router()


@router.message(Command(commands='cancel'), StateFilter(default_state), IsAdmin())
async def process_cancel_command(message: Message):
    await message.answer(text=LEXICON_ADMIN['/cancel1'],
                         reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands='cancel'), ~StateFilter(default_state), IsAdmin())
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_ADMIN['/cancel2'],
                         reply_markup=ReplyKeyboardRemove())
    await state.clear()


@router.message(Command(commands='allarticles'), IsAdmin())
async def process_allarticles_command(message: Message):
    await message.answer(
        text=await print_articles(data=await get_articles(secret_articles=True)), disable_web_page_preview=True)


@router.message(Command(commands=['addarticle']), StateFilter(default_state), IsAdmin())
async def process_addarticle_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_ADMIN['fill_title'], reply_markup=ReplyKeyboardRemove())
    await state.set_state(FSMAddArticle.fill_title)


@router.message(StateFilter(FSMAddArticle.fill_title), IsAdmin())
async def process_title_sent(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer(text=LEXICON_ADMIN['fill_emoji'])
    await state.set_state(FSMAddArticle.fill_emoji)


@router.message(StateFilter(FSMAddArticle.fill_emoji), IsAdmin())
async def process_emoji_sent(message: Message, state: FSMContext):
    await state.update_data(emoji=message.text)
    await message.answer(text=LEXICON_ADMIN['fill_link'])
    await state.set_state(FSMAddArticle.fill_link)


@router.message(StateFilter(FSMAddArticle.fill_link), IsAdmin())
async def process_link_sent(message: Message, state: FSMContext):
    await state.update_data(link=message.text)
    await message.answer(text=LEXICON_ADMIN['fill_keywords'])
    await state.set_state(FSMAddArticle.fill_keywords)


@router.message(StateFilter(FSMAddArticle.fill_keywords), IsAdmin())
async def process_keywords_sent(message: Message, state: FSMContext):
    await state.update_data(keywords=message.text.lower())
    await message.answer(text=LEXICON_ADMIN['fill_section'], reply_markup=await create_sections_keyboard())
    await state.set_state(FSMAddArticle.fill_section)


@router.message(StateFilter(FSMAddArticle.fill_section), IsAdmin())
async def process_section_sent(message: Message, state: FSMContext):
    await state.update_data(section=message.text)
    await message.answer(text=LEXICON_ADMIN['fill_position'].format(
        section=message.text,
        articles=await print_articles(data=await get_articles(only_section=message.text, secret_articles=True),
                                      new_article=True)),
        disable_web_page_preview=True,
        reply_markup=ReplyKeyboardRemove())
    await state.set_state(FSMAddArticle.fill_position)


@router.message(StateFilter(FSMAddArticle.fill_position), IsAdmin())
async def process_position_sent(message: Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer(text=LEXICON_ADMIN['fill_is_published'], reply_markup=await create_is_published_keyboard())
    await state.set_state(FSMAddArticle.fill_is_published)


@router.message(StateFilter(FSMAddArticle.fill_is_published),
                Text(text=[LEXICON_KEYBOARDS_ADMIN['is_published_button'],
                           LEXICON_KEYBOARDS_ADMIN['not_is_published_button']]), IsAdmin())
async def process_is_published_sent(message: Message, state: FSMContext):
    await state.update_data(is_published=message.text[-1:])
    user_dict[message.from_user.id] = await state.get_data()

    await message.answer(text=LEXICON_ADMIN['check_data'].format(**user_dict[message.from_user.id]),
                         disable_web_page_preview=True,
                         reply_markup=await create_allow_publishing_keyboard())

    await state.set_state(FSMAddArticle.allow_publishing)


@router.message(StateFilter(FSMAddArticle.allow_publishing),
                Text(text=[LEXICON_KEYBOARDS_ADMIN['allow_publishing_button'],
                           LEXICON_KEYBOARDS_ADMIN['not_allow_publishing_button']]), IsAdmin())
async def process_allow_publishing_sent(message: Message, state: FSMContext):
    if message.text == LEXICON_KEYBOARDS_ADMIN['allow_publishing_button']:
        await sql_add_article(await handle_article_data(user_dict[message.from_user.id]))
        await message.answer(text=LEXICON_ADMIN['success'], reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text=LEXICON_ADMIN['/cancel2'], reply_markup=ReplyKeyboardRemove())
    await state.clear()


@router.message(StateFilter(FSMAddArticle.fill_is_published), IsAdmin())
@router.message(StateFilter(FSMAddArticle.allow_publishing), IsAdmin())
async def warning_not_is_available(message: Message):
    await message.answer(text=LEXICON_ADMIN['warning_keyboard'])

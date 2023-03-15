import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import load_config
from states import admin_states
from keyboards.set_menu import set_user_menu, set_admin_menu
from handlers import user_handlers, admin_handlers, other_handlers
from database.sqlite import sql_start

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config = load_config(r'.env')

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=admin_states.storage)

    await set_user_menu(bot)
    await set_admin_menu(bot)

    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    
    sql_start(config.db.database)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped')

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers.other import other_router
from handlers.user import user_router
from middlewares.inner import FirstInnerMiddleware
from middlewares.outer import (
    FirstOuterMiddleware,
    ThrottlingMiddleware
)
from middlewares.i18n import TranslatorMiddleware
from lexicon.lexicon import LEXICON_EN, LEXICON_RU


translations = {
    'default': 'ru',
    'en': LEXICON_EN,
    'ru': LEXICON_RU
}

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)

async def main():
    config = load_config()

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(user_router)
    dp.include_router(other_router)

    dp.update.middleware(TranslatorMiddleware())
    dp.update.outer_middleware(FirstOuterMiddleware())
    other_router.message.outer_middleware(ThrottlingMiddleware())

    await dp.start_polling(bot, _translations=translations)

if __name__ == '__main__':
    asyncio.run(main())

import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from filters.filters import MyFalseFilter, MyTrueFilter
from lexicon.lexicon import LEXICON_RU

logger = logging.getLogger(__name__)

user_router = Router()

@user_router.message(Command('start'), MyTrueFilter())
async def process_start_command(message: Message, i18n: dict[str, str]):
    logger.debug('Вошли в хэндлер, обрабатывающий команду /start')
    button = InlineKeyboardButton(
        text=i18n.get('button'),
        callback_data='button_pressed'
    )
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer(text=i18n.get('/start'), reply_markup=markup)
    logger.debug('Выходим из хэндлера, обрабатывающего команду /start')


@user_router.callback_query(F.data, MyTrueFilter())
async def process_button_click(callback: CallbackQuery, i18n: dict[str, str]):
    logger.debug('Вошли в хэндлер, обрабатывающий нажатие на инлайн-кнопку')
    await callback.answer(text=i18n.get('button_pressed'))
    logger.debug('Выходим из хэндлера, обрабатывающего нажатие на инлайн-кнопку')


@user_router.message(F.text, MyFalseFilter())
async def process_text(message: Message):
    logger.debug('Вошли в хэндлер, обрабатывающий текст')
    logger.debug('Выходим из хэндлера, обрабатывающего текст')

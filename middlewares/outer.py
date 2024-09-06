import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from cachetools import TTLCache


logger = logging.getLogger(__name__)

CACHE = TTLCache(maxsize=10_000, ttl=10)

class FirstOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )
        print(data)
        print(data.get('event_from_user'))

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        return result


class ThrottlingMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data.get('event_from_user')

        if user.id in CACHE:
            return

        CACHE[user.id] = True

        return await handler(event, data)

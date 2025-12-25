import asyncio
from aiogram import Bot, Dispatcher
from chat_tracker.config import load_config
from admin_bot.presentation.handlers import router
from storage.bot_repository import BotRepository
from bots.infrastructure.telegram_client import TelegramClient


async def main():
    config = load_config()
    repo = BotRepository()
    tg = TelegramClient()

    bot = Bot(token=config.bot_token)
    dp = Dispatcher()

    dp.include_router(start.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

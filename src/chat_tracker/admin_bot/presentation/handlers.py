from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bots.application.bot_service import BotService

router = Router()


@router.message(Command("addbot"))
async def add_bot(message: Message, bot_service: BotService):
    token = message.text.split(maxsplit=1)[1]

    bot = await bot_service.add_bot(token)
    await message.answer(f"Bot @{bot.username} have been added")

from aiogram import Bot
from aiogram.exceptions import TelegramUnauthorizedError


class TelegramClient:
    def __init__(self, webhook_base_url: str):
        self.webhook_base_url = webhook_base_url

    async def register_bot(self, token: str) -> dict:
        try: 
            bot = Bot(token)
            me = await bot.get_me()

            await bot.set_webhook(
                url=f"{self.webhook_base_url}/{me.id}",
                allowed_updates=["message", "my_chat_member"],
            )

            return {
                "id": me.id,
                "username": me.username,
                "token": token,
            }
        except TelegramUnauthorizedError:
            raise ValueError("Invalid token")
from bots.domain.bot import ManagedBot
from storage.bot_repository import BotRepository
from bots.infrastructure.telegram_client import TelegramClient


class BotService:
    def __init__(self, repo: BotRepository, tg: TelegramClient):
        self.repo = repo
        self.tg = tg

    async def add_bot(self, token: str) -> ManagedBot:
        data = await self.tg.register_bot(token)

        bot = ManagedBot(
            id=data["id"],
            username=data["username"],
            token=data["token"],
        )

        self.repo.add(bot)
        return bot
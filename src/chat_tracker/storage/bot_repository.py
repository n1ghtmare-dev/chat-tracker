from typing import Dict
from bots.domain.bot import ManagedBot


class BotRepository:
    def __init__(self):
        self._bots: Dict[int, ManagedBot] = {}

    def add(self, bot: ManagedBot):
        self._bots[bot.id] = bot

    def get(self, bot_id: int) -> ManagedBot | None:
        return self._bots.get(bot_id)
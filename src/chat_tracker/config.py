from dataclasses import dataclass
import os
from dotenv import load_dotenv


load_dotenv()

@dataclass(frozen=True)
class Config:
    admin_bot_token: str

    webhook_base_url: str
    webhook_path: str = "/webhook"

    debug: bool = False


def load_config() -> Config:
    return Config(
        admin_bot_token=os.getenv("BOT_TOKEN"),
        webhook_base_url=os.getenv("WEBHOOK_BASE_URL"),
        debug=os.getenv("DEBUG", "false").lower() == "true",
        )


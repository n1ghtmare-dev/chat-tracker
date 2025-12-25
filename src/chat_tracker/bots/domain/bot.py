from dataclasses import dataclass


@dataclass
class ManagedBot:
    id: int
    username: str
    token: str
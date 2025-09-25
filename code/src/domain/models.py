from dataclasses import dataclass
from typing import Optional

@dataclass
class Repository:
    name: str
    owner: str
    full_name: str
    stargazers: int
    url: str
    description: Optional[str] = None

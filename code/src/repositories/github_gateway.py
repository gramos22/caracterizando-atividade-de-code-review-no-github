from typing import Protocol, List
from src.domain.models import Repository

class GitHubGateway(Protocol):
    def search_top_repositories(self, language: str, limit: int) -> List[Repository]:
        ...

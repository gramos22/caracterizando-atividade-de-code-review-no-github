from typing import Protocol, List
from src.domain.models import Repository, PullRequest

class GitHubGateway(Protocol):
    def search_top_repositories(self, language: str, limit: int) -> List[Repository]:
        ...
    def get_pull_requests(self, owner: str, name: str, limit: int) -> List[PullRequest]:
        ...

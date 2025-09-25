from typing import List
from src.repositories.github_gateway import GitHubGateway
from src.domain.models import Repository
import json

def collect_top_repositories(gateway: GitHubGateway, language: str, limit: int) -> List[Repository]:
    repos = gateway.search_top_repositories(language=language, limit=limit)
    return repos

def save_repositories(repos: List[Repository], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump([repo.__dict__ for repo in repos], f, ensure_ascii=False, indent=2)

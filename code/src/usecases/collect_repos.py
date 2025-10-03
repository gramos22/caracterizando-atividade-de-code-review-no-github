from typing import List
from src.repositories.github_gateway import GitHubGateway
from src.domain.models import Repository
import json

def collect_top_repositories(gateway: GitHubGateway, language: str, limit: int, min_prs: int) -> List[Repository]:
    repos = gateway.search_top_repositories(language=language, limit=limit, min_prs=min_prs)
    return repos

def save_repositories(repos: List[Repository], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump([
            {
                "name": repo.name,
                "owner": repo.owner,
                "full_name": repo.full_name,
                "stargazers": repo.stargazers,
                "url": repo.url,
                "description": repo.description,
                "pull_requests_count": repo.pull_requests_count
            }
            for repo in repos
        ], f, ensure_ascii=False, indent=2)

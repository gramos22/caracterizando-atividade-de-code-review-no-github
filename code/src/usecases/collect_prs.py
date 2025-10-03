from typing import List
from src.repositories.github_gateway import GitHubGateway
from src.domain.models import PullRequest
import json

def collect_pull_requests(gateway: GitHubGateway, owner: str, name: str, limit: int) -> List[PullRequest]:
    try:
        prs = gateway.get_pull_requests(owner, name, limit)
        return prs if prs is not None else []
    except Exception as e:
        print(f"Erro ao coletar PRs de {owner}/{name}: {e}")
        return []

def save_pull_requests(prs: List[PullRequest], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump([{
            "number": pr.number,
            "title": pr.title,
            "author": pr.author,
            "created_at": pr.created_at.isoformat(),
            "closed_at": pr.closed_at.isoformat(),
            "merged": pr.merged,
            "additions": pr.additions,
            "deletions": pr.deletions,
            "changed_files": pr.changed_files,
            "description_length": pr.description_length,
            "participants_count": pr.participants_count,
            "comments_count": pr.comments_count,
            "review_duration_hours": pr.review_duration_hours,
            "reviews": [{"author": r.author, "submitted_at": r.submitted_at.isoformat()} for r in pr.reviews],
            "url": pr.url
        } for pr in prs], f, ensure_ascii=False, indent=2)
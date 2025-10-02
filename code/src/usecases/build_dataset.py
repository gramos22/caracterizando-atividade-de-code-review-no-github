import json
import csv
from typing import List
from src.repositories.github_gateway import GitHubGateway
from src.usecases.collect_prs import collect_pull_requests
from src.domain.models import PullRequest, Repository

def load_repositories(path: str) -> List[Repository]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    repos = [Repository(**repo) for repo in data]
    return repos

def build_dataset(gateway: GitHubGateway, repos: List[Repository], prs_limit: int, output: str) -> None:
    fieldnames = [
        "repo_full_name",
        "repo_stars",
        "pull_requests_count",
        "pr_number",
        "title",
        "author",
        "created_at",
        "closed_at",
        "merged",
        "additions",
        "deletions",
        "changed_files",
        "description_length",
        "participants_count",
        "comments_count",
        "review_duration_hours",
        "url"
    ]
    with open(output, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for repo in repos:
            prs: List[PullRequest] = collect_pull_requests(gateway, repo.owner, repo.name, prs_limit)
            for pr in prs:
                writer.writerow({
                    "repo_full_name": repo.full_name,
                    "repo_stars": repo.stargazers,
                    "pull_requests_count": repo.pull_requests_count,
                    "pr_number": pr.number,
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
                    "url": pr.url
                })

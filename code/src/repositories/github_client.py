from typing import List
from datetime import datetime
from src.repositories.github_gateway import GitHubGateway
from src.adapters.http_client import HTTPClient
from src.domain.models import Repository, PullRequest, Review
from src.constants.queries import SEARCH_REPOSITORIES, GET_PULL_REQUESTS

class GitHubGraphQLClient(GitHubGateway):
    def __init__(self, http_client: HTTPClient):
        self.http = http_client

    def search_top_repositories(self, language: str, limit: int, min_prs: int = 0) -> List[Repository]:
        repos = []
        q = f"language:{language} sort:stars"
        after = None
        per_page = 100

        while len(repos) < limit:
            variables = {
                "q": q,
                "first": min(per_page, limit - len(repos)),
                "after": after
            }
            payload = {"query": SEARCH_REPOSITORIES, "variables": variables}
            result = self.http.post(payload)
            search = result.get("data", {}).get("search", {})
            nodes = search.get("nodes", [])
            page_info = search.get("pageInfo", {})

            for node in nodes:
                pr_count = node.get("pullRequests", {}).get("totalCount", 0)
                if pr_count < min_prs:
                    continue
                repos.append(Repository(
                    name=node.get("name"),
                    owner=node.get("owner", {}).get("login"),
                    full_name=f"{node.get('owner', {}).get('login')}/{node.get('name')}",
                    stargazers=node.get("stargazerCount", 0),
                    url=node.get("url"),
                    description=node.get("description"),
                    pull_requests_count=pr_count,
                ))
                if len(repos) >= limit:
                    break

            if not page_info.get("hasNextPage"):
                break
            after = page_info.get("endCursor")

        return repos
    
    def get_pull_requests(self, owner: str, name: str, limit: int) -> List[PullRequest]:
        variables = {"owner": owner, "name": name, "first": limit}
        payload = {"query": GET_PULL_REQUESTS, "variables": variables}
        result = self.http.post(payload)
        nodes = result.get("data", {}).get("repository", {}).get("pullRequests", {}).get("nodes", [])
        prs = []
        for node in nodes:
            if not node.get("closedAt") or not node.get("createdAt"):
                continue
            created_at = datetime.fromisoformat(node["createdAt"].replace("Z", "+00:00"))
            closed_at = datetime.fromisoformat(node["closedAt"].replace("Z", "+00:00"))
            reviews = []
            for r in node.get("reviews", {}).get("nodes", []):
                if not r.get("submittedAt"):
                    continue
                reviews.append(Review(
                    author=r.get("author", {}).get("login"),
                    submitted_at=datetime.fromisoformat(r["submittedAt"].replace("Z", "+00:00"))
                ))
            if len(reviews) == 0:
                continue
            delta = (closed_at - created_at).total_seconds()
            if delta < 3600:
                continue
            prs.append(PullRequest(
                number=node.get("number"),
                title=node.get("title"),
                author=node.get("author", {}).get("login"),
                created_at=created_at,
                closed_at=closed_at,
                merged=node.get("merged"),
                additions=node.get("additions", 0),
                deletions=node.get("deletions", 0),
                changed_files=node.get("changedFiles", 0),
                description_length=len(node.get("bodyText", "") or ""),
                participants_count=node.get("participants", {}).get("totalCount", 0),
                comments_count=node.get("comments", {}).get("totalCount", 0),
                review_duration_hours=self.__convert_to_hours(delta),
                reviews=reviews,
                url=node.get("url")
            ))
        return prs
    
    def __convert_to_hours(self, delta_seconds: float) -> float:
        return ("%.2f" % (delta_seconds / 3600.0))

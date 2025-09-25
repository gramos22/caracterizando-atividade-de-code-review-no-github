from typing import List
from src.repositories.github_gateway import GitHubGateway
from src.adapters.http_client import HTTPClient
from src.domain.models import Repository

class GitHubGraphQLClient(GitHubGateway):
    def __init__(self, http_client: HTTPClient):
        self.http = http_client

    def search_top_repositories(self, language: str, limit: int) -> List[Repository]:
        per_page = 50
        query = """
query($q:String!, $first:Int!) {
  search(query: $q, type: REPOSITORY, first: $first) {
    nodes {
      ... on Repository {
        name
        owner { login }
        stargazerCount
        url
        description
      }
    }
  }
}
"""
        q = f"language:{language} sort:stars"
        variables = {"q": q, "first": min(limit, per_page)}
        payload = {"query": query, "variables": variables}
        result = self.http.post(payload)
        nodes = result.get("data", {}).get("search", {}).get("nodes", [])
        repos = []
        for node in nodes:
            repos.append(Repository(
                name=node.get("name"),
                owner=node.get("owner", {}).get("login"),
                full_name=f"{node.get('owner', {}).get('login')}/{node.get('name')}",
                stargazers=node.get("stargazerCount", 0),
                url=node.get("url"),
                description=node.get("description"),
            ))
        return repos[:limit]

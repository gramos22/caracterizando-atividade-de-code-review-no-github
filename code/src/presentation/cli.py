import click
from src.config.config import get_github_token
from src.adapters.http_client import HTTPClient
from src.repositories.github_client import GitHubGraphQLClient
from src.usecases.collect_repos import collect_top_repositories, save_repositories
from src.usecases.collect_prs import collect_pull_requests, save_pull_requests

@click.group()
def cli():
    pass

@cli.command()
@click.option("--language", "-l", default="Java", show_default=True)
@click.option("--limit", "-n", default=50, show_default=True)
@click.option("--output", "-o", default="repos.json", show_default=True)
def collect_repos(language, limit, output):
    token = get_github_token()
    http = HTTPClient(token)
    client = GitHubGraphQLClient(http)
    repos = collect_top_repositories(client, language, int(limit))
    save_repositories(repos, output)
    click.echo(f"Foram salvos {len(repos)} repositórios em {output}")

@cli.command()
@click.option("--repo", "-r", required=True, help="Formato: owner/name")
@click.option("--limit", "-n", default=30, show_default=True)
@click.option("--output", "-o", default="prs.json", show_default=True)
def collect_prs(repo, limit, output):
    token = get_github_token()
    http = HTTPClient(token)
    client = GitHubGraphQLClient(http)
    owner, name = repo.split("/")
    prs = collect_pull_requests(client, owner, name, int(limit))
    save_pull_requests(prs, output)
    click.echo(f"Foram salvos {len(prs)} pull requests em {output}")

if __name__ == "__main__":
    cli()

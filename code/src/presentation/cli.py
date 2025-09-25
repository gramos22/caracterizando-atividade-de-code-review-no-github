import click
from src.config.config import get_github_token
from src.adapters.http_client import HTTPClient
from src.repositories.github_client import GitHubGraphQLClient
from src.usecases.collect_repos import collect_top_repositories, save_repositories

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

if __name__ == "__main__":
    cli()

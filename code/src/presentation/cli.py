import click
from src.config.config import get_github_token
from src.adapters.http_client import HTTPClient
from src.repositories.github_client import GitHubGraphQLClient
from src.usecases.collect_repos import collect_top_repositories, save_repositories
from src.usecases.collect_prs import collect_pull_requests, save_pull_requests
from src.usecases.build_dataset import load_repositories, build_dataset as build_dataset_usecase

@click.group()
def cli():
    pass

@cli.command()
@click.option("--language", "-l", default="Java", show_default=True)
@click.option("--limit", "-n", default=50, show_default=True)
@click.option("--min-prs", "-m", default=100, show_default=True, help="Número mínimo de PRs fechados/merged")
@click.option("--output", "-o", default="repos.json", show_default=True)
def collect_repos(language, limit, min_prs, output):
    token = get_github_token()
    http = HTTPClient(token)
    client = GitHubGraphQLClient(http)
    repos = collect_top_repositories(client, language, int(limit), int(min_prs))
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

@cli.command(name="build-dataset")
@click.option("--repos", "-r", default="repos.json", show_default=True)
@click.option("--prs-limit", "-p", default=20, show_default=True, help="Número de PRs por repositório")
@click.option("--output", "-o", default="dataset.csv", show_default=True)
def build_dataset_cmd(repos, prs_limit, output):
    token = get_github_token()
    http = HTTPClient(token)
    client = GitHubGraphQLClient(http)

    repos_list = load_repositories(repos)
    build_dataset_usecase(client, repos_list, int(prs_limit), output)
    click.echo(f"Dataset salvo em {output}")

if __name__ == "__main__":
    cli()

import json

def main():
    with open("repos.json", "r", encoding="utf-8") as f:
        repos = json.load(f)

    repo_count = len(repos)
    total_prs = sum(r.get("pull_requests_count", 0) for r in repos)
    avg_prs = total_prs / repo_count if repo_count > 0 else 0

    print(f"Quantidade de repositórios no arquivo: {repo_count}")
    print(f"Total de PRs (merged/closed): {total_prs}")
    print(f"Média de PRs por repositório: {avg_prs:.2f}")

if __name__ == "__main__":
    main()

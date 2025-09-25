from dotenv import load_dotenv
import os

load_dotenv()

def get_github_token() -> str:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN not set")
    return token

from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime

@dataclass
class Repository:
    name: str
    owner: str
    full_name: str
    stargazers: int
    url: str
    description: Optional[str] = None
    pull_requests_count: int = 0

@dataclass
class Review:
    author: str
    submitted_at: datetime

@dataclass
class PullRequest:
    number: int
    title: str
    author: str
    created_at: datetime
    closed_at: datetime
    merged: bool
    additions: int
    deletions: int
    changed_files: int
    description_length: int
    participants_count: int
    comments_count: int
    review_duration_hours: float
    reviews: List[Review]
    url: str

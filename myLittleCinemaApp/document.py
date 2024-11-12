from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Review:
    user: str
    review: str
    rating: int
    review_date: datetime = field(default_factory=datetime.now)

@dataclass
class MovieDocument:
    title: str
    release_date: datetime
    director: str
    genres: List[str]
    reviews: List[Review] = field(default_factory=list)

@dataclass
class UserMoviesDocument:
    user_id: str
    favorites: List[dict] = field(default_factory=list)

@dataclass
class ActorDocument:
    actor_id: str
    name: str
    birthdate: datetime
    filmography: List[dict] = field(default_factory=list)
    biography: Optional[str] = None

@dataclass
class CinemaDocument:
    cinema_id: str
    name: str
    location: str
    showtimes: List[dict] = field(default_factory=list)

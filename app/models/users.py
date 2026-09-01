# Handle Single User
from dataclasses import dataclass
from repositories.user_repository import add_user, get_user, update_user, delete_user

@dataclass
class user:
    id: int
    name: str
    email: str


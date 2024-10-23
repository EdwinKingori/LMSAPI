from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    is_active: bool
    bio: Optional[str]

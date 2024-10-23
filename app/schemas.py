from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List


class User(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class config:
        orm_mode = True

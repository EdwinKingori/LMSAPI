from fastapi import FastAPI, APIRouter
from typing import Optional, List
from .. import schemas

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get("/", response_model=List[schemas.User])
async def get_users():
    pass


@router.post("/")
async def create_user(user: schemas.User):
    user.append(user)
    return "success"


@router.get("/users/{id}")
async def get_user(id: int):
    pass

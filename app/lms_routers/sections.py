from fastapi import FastAPI, APIRouter
from typing import Optional, List
from .. import schemas


router = APIRouter(
    prefix="/sections",
    tags=['sections']
)


@router.get("/")
def get_course():
    pass


@router.post("/")
def create_course():
    pass


@router.get("/{id}")
def get_courses(id: int):
    pass


@router.put("/{id}")
def update_course(id: int):
    pass


@router.delete("/{id}")
def delete_course(id: int):
    pass

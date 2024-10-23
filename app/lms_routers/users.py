from fastapi import FastAPI, APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional, List
from .. import schemas, models
from .. database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get("/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User,  db: Session = Depends(get_db)):

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/users/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.id == models.User.id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=(f"user with {id} not found!"))
    return user

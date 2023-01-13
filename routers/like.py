from routers.schemas import LikeBase, UserAuth
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_like
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/like',
    tags=['like']
)


@router.post('')
def create(request: LikeBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_like.create(db, request)


@router.get('/delete/{id}')
def delete(like_id: int ,db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    db_like.delete(db, like_id, current_user.id)

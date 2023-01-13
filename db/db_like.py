from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.models import DbLike, DbPost
from routers.schemas import LikeBase


def create(db: Session, request: LikeBase):
    post = db.query(DbPost).filter(DbPost.id == request.post_id).first()
    if request.user_id == post.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='You cannot like your own post')
    else:
        new_like = DbLike(
            user_id=request.user_id,
            post_id=request.post_id,
            username=request.username
        )
        db.add(new_like)
        db.commit()
        db.refresh(new_like)
        return new_like


def delete(db: Session, like_id: int, user_id: int):
    like = db.query(DbLike).filter(DbLike.id == like_id).first()
    if not like:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Like with id {like_id} not found')
    if like.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only like creator can delete a like')
    db.delete(like)
    db.commit()
    return 'ok'

from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbPost', back_populates='user')


class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('DbUser', back_populates='items')
    comments = relationship('DbComment', back_populates='post')
    likes = relationship('DbLike', back_populates='post')


class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    username = Column(String)
    timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("DbPost", back_populates="comments")


class DbLike(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    post = relationship('DbPost', back_populates='likes')
    __table_args__ = (
        UniqueConstraint(post_id, user_id),
    )


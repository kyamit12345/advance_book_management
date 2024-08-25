from sqlalchemy import Column, ForeignKey, Integer, String
from app.db import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "books"
    id= Column(Integer, primary_key=True, index=True)
    title= Column(String, index=True)
    author= Column(String, index=True)
    genre= Column(String, index=True)
    year_published= Column(Integer, index=True)
    summary=Column(String)

class Review(Base):
    __tablename__="reviews"
    id= Column(Integer, primary_key=True, index=True)
    book_id=Column(Integer, ForeignKey("books.id"),nullable=False)
    user_id= Column(Integer,index=True)
    review_txt= Column(String, index=True)
    rating= Column(Integer)
    book=relationship("Book", back_populates="reviews")



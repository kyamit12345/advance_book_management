from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import BookInsert,BookRead, ReviewRead
from app.crud import book_insert, get_all_books,get_book, reviews_for_book,update_book,delete_book,review_insert
from app.db import get_session

router=APIRouter()

@router.post("/books/",response_model=BookInsert)
async def insert_book(book:BookInsert,session:AsyncSession=Depends(get_session)):
    return await book_insert(session,book)

@router.get("/books/{id}",response_model=BookRead)
async def get_book(id:int,session:AsyncSession=Depends(get_session)):
    book=await get_book(session,id)
    if book is None:
        raise HTTPException(status_code=404,detail="Book Not Found.")
    return book

@router.put("/books/{id}",response_model=BookRead)
async def update_book(id:int,book:BookInsert,session:AsyncSession=Depends(get_session)):
    updated_book=await update_book(session,id,book)
    if updated_book is None:
        raise HTTPException(status_code=404,detail="Book Not Found.")
    return updated_book

@router.delete("/books/{id}")
async def delete_book(id:int,session:AsyncSession=Depends(get_session)):
    book=await delete_book(session,id)
    if book is None:
        raise HTTPException(status_code=404,detail="Book Not Found.")
    return {"Book deleted successfully."}

@router.get("/books/",response_model=List[BookRead])
async def get_books(session:AsyncSession=Depends(get_session)):
    books=await get_all_books(session)
    return books

@router.post("/reviews/",response_model=ReviewRead)
async def create_review(review:ReviewRead,session:AsyncSession=Depends(get_session)):
    return await review_insert(session,review)

@router.get("/reviews{id}/",response_model=List[BookRead])
async def get_reviews(session:AsyncSession=Depends(get_session)):
    books=await reviews_for_book(session,id)
    return books




from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Book, Review
from app.schemas import BookInsert,ReviewInsert

async def book_insert(db:AsyncSession,book:BookInsert):
    book_to_add=Book(title=book.title,author=book.author)
    db.add(book_to_add)
    await db.commit()
    await db.refresh(book_to_add)
    return book_to_add

async def get_book(db:AsyncSession,id:int):
    result=await db.execute(select(Book).where(Book.id==id))
    return result.scalar_one_or_none()

async def update_book(db:AsyncSession,id:int, book:BookInsert):
    book_by_id= await db.execute(select(Book).where(Book.id==id))
    book_to_update= book_by_id.scalar_one_or_none()
    if(book_to_update):
        book_to_update.title=book.title
        book_to_update.author= book.author
        await db.commit()
        await db.refresh(book_to_update)
    return book_to_update

async def delete_book(db:AsyncSession, id:int):
    book_by_id= await db.execute(select(Book).where(Book.id==id))
    book_to_delete= book_by_id.scalar_one_or_none()
    if(book_to_delete):
        await db.delete(book_to_delete)
        await db.commit()
    return book_to_delete

    
async def get_all_books(db:AsyncSession):
    books=await db.execute(select(Book))
    return books.scalars.all()

async def review_insert(db:AsyncSession,review:ReviewInsert):
    review=Review(book_id=review.book_id,user_id=review.user_id,review_txt=review.review_txt,rating=review.rating)
    db.add(review)
    await db.commit()
    await db.refresh(review)
    return review

async def reviews_for_book(db:AsyncSession,book_id:int):
    reviews=await db.execute(select(Review).where(Review.book_id==book_id))
    return reviews.scalars.all()
from pydantic import BaseModel

class BookInsert(BaseModel):
    title:str
    author:str
    genre:str
    year_published:int
    summary:str

class BookRead(BaseModel):
    id:int
    title:str
    author:str
    genre:str
    year_published:int
    summary:str

    class Config_Dict:
        from_attributes=True

class ReviewInsert(BaseModel):
    book_id:int
    review_txt:str
    rating:int
    user_id:int

class ReviewRead(BaseModel):
    id:int
    book_id:int
    review_txt:str
    rating:int
    user_id:int

    class ConfigDict:
        from_attributes=True
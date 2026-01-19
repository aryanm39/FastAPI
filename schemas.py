from pydantic import BaseModel,EmailStr
class UserCreate(BaseModel):
    username: EmailStr
    password: str

class BlogCreate(BaseModel):
    title:str
    body:str
       
class BlogResponse(BaseModel):
    id: int
    title: str
    body: str
    author: str

    class Config:
        from_attributes = True

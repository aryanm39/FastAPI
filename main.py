from fastapi import FastAPI, Depends, HTTPException,status
from sqlalchemy.orm import Session
from db import get_db, create_table
from models import User,Blog
from services import create_access_token, hash_password, verify_password,get_current_user
from schemas import UserCreate,BlogCreate,BlogResponse
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()
security = HTTPBearer()
create_table()
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"username": new_user.username, "id": new_user.id}

@app.post('/login')
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": db_user.username,"role": db_user.role,"id": db_user.id})
    return {"access_token": access_token,"user": {"username": db_user.username,"role": db_user.role}}

@app.get("/blogs", response_model=List[BlogResponse])
def get_blogs(db: Session = Depends(get_db)):
    return db.query(Blog).all()

@app.get("/blogs/{blog_id}", response_model=BlogResponse)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@app.post("/blogs")
def create_blog(
    blog: BlogCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    new_blog = Blog(title=blog.title,body=blog.body,author=current_user["username"])
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete("/blogs/{blog_id}")
def delete_blog(
    blog_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    if current_user["role"] == "admin":
        pass

    elif blog.author != current_user["username"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(blog)
    db.commit()
    return {"status": "deleted"}



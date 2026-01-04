from fastapi import FastAPI, HTTPException, Depends
import psycopg

from app.config import settings
from app.db import engine,get_db
from app.models import Base,User
from app.schemas import UserCreate

from sqlalchemy.orm import Session

from app.security import hash_password


app = FastAPI(title="TaskApp", debug=True)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    try:
        # db-check 用 psycopg 直接连（简单直观）
        with psycopg.connect(settings.DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                row = cur.fetchone()
        return {"db": "ok", "select": row[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        email=user.email,
        password_hasheddddd=hash_password(user.password)  # ⚠️ 先明文，下一步再加 hash
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "email": new_user.email
    }


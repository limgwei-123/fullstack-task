from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

def _to_sqlalchemy_url(url: str) -> str:
    # 你现在 .env 用的是 postgresql:// (psycopg DSN)
    # SQLAlchemy 需要 postgresql+psycopg://
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+psycopg://", 1)
    return url

engine = create_engine(_to_sqlalchemy_url(settings.DATABASE_URL), pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

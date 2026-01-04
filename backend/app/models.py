from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Boolean, ForeignKey

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__ = "users"
  id: Mapped[int] = mapped_column(primary_key=True)
  email: Mapped[str] = mapped_column(String(255), nullable=False)
  password_hashed: Mapped[str] = mapped_column(String(255), nullable=False)

class Task(Base):
  __tablename__ = "tasks"
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(200), nullable=False)
  completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
  owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
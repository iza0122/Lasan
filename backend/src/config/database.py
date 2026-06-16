import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Sử dụng SQLite cho môi trường local và PostgreSQL cho production (hoặc Supabase)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./home_management.db")

# Nếu dùng SQLite, cần cấu hình thêm check_same_thread=False
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency để lấy database session cho từng request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

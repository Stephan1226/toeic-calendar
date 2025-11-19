from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "toeic_calendar")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DayRecord(Base):
    __tablename__ = "day_records"
    
    id = Column(Integer, primary_key=True, index=True)
    day = Column(Integer, unique=True, nullable=False)
    checked = Column(Boolean, default=False)
    source = Column(String(500), default="")
    notion_link = Column(String(500), default="")

def init_db():
    Base.metadata.create_all(bind=engine)
    
    # 초기 30일 데이터 생성
    db = SessionLocal()
    try:
        existing_count = db.query(DayRecord).count()
        if existing_count == 0:
            for day in range(1, 31):
                record = DayRecord(day=day, checked=False, source="", notion_link="")
                db.add(record)
            db.commit()
    finally:
        db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

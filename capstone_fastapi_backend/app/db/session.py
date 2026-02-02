from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
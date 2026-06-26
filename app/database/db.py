from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from config import Config


DATABASE_URL = f"sqlite:///{Config.DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


def get_session():
    return SessionLocal()


def init_db():

    from app.database.models import Base

    Base.metadata.create_all(bind=engine)
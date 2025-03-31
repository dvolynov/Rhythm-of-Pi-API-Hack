from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
import os, dotenv, datetime

dotenv.load_dotenv()


engine = create_engine(url=f"postgresql+psycopg2://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}?sslmode={os.getenv('DB_SSLMODE')}")
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id         = Column(Integer, primary_key=True, index=True)
    username   = Column(String(150), nullable=True, unique=True)
    password   = Column(String(150), nullable=True)
    hash       = Column(String(255), nullable=False)
    level      = Column(Integer, nullable=False)
    ip         = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    song = relationship('Song', back_populates='user')


class Level(Base):
    __tablename__ = 'level'

    id         = Column(Integer, primary_key=True, index=True)
    title      = Column(String(255), nullable=False)
    tags       = Column(String(255), nullable=False)
    url        = Column(String(500), nullable=False)
    image_url  = Column(String(500), nullable=False)
    duration   = Column(Integer, nullable=False)
    level      = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Song(Base):
    __tablename__ = 'song'

    id         = Column(Integer, primary_key=True, index=True)
    title      = Column(String(255), nullable=False)
    tags       = Column(String(255), nullable=False)
    url        = Column(String(500), nullable=False)
    image_url  = Column(String(500), nullable=False)
    task_id    = Column(String(255), nullable=False)
    duration   = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id    = Column(Integer, ForeignKey('user.id'))

    user       = relationship('User', back_populates='song')


Base.metadata.create_all(bind=engine)
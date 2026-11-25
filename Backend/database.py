
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///./gta.db")

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="player")


Base.metadata.create_all(engine)

from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(100))
    name = Column(String(100), nullable=True)
    surname = Column(String(100), nullable=True)
    age = Column(Integer, nullable=True)
    city = Column(String(50), nullable=True)
    tlg_link = Column(String(256), nullable=True)
    rate = Column(Float, nullable=True)
    hard_rate = Column(Float, nullable=True)
    soft_rate = Column(Float, nullable=True)
    employee = Column(Boolean, default=False)
    stack_id = Column(Integer, ForeignKey('stack.id'), nullable=True)
    stack = relationship('Stack', uselist=False)


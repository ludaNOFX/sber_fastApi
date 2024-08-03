from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Stack(Base):
    __tablename__ = 'stack'
    id = Column(Integer, primary_key=True)
    names = Column(String(256), nullable=False)
    
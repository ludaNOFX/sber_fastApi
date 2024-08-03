from typing import Optional, Sequence, List

from pydantic import BaseModel


class StackBase(BaseModel):
    names: Optional[str] = None


# Свойства, которые необходимо получить при создании
class StackCreate(StackBase):
    names: str


# Свойства, которые необходимо получить при обновлении
class StackUpdate(StackBase):
    names: str


class StackInDBBase(StackBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Свойства, которые возвращает API
class Stack(StackInDBBase):
    pass


# Свойства хранящиеся в БД
class StackInDB(StackInDBBase):
    pass


class Stacks(BaseModel):
    results: Sequence[Stack]

from typing import Optional, Sequence, List

from pydantic import BaseModel, EmailStr, HttpUrl


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None
    tlg_link: Optional[HttpUrl] = None
    rate: Optional[float] = None
    hard_rate: Optional[float] = None
    soft_rate: Optional[float] = None
    employee: Optional[bool] = None
    stack_id: Optional[int] = None


# Свойства, которые необходимо получить при создании
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Свойства, которые необходимо получить при обновлении
class UserUpdate(UserBase):
    password: Optional[str]


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Свойства, которые возвращает API
class User(UserInDBBase):
    pass


# Свойства хранящиеся в БД
class UserInDB(UserInDBBase):
    password_hash: str


class UsersInDB(BaseModel):
    results: Sequence[User]


class Classes(BaseModel):
    high: List[User]
    mid: List[User]
    low: List[User]

from typing import Generator, Optional

from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.core.auth import oauth2_scheme
from app.core.config import settings
from app.models.users import Users
from app.models.stack import Stack
from app.schemas.token import TokenPayload
from app.crud.crud_user import user


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> Users:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False}
        )
        sub: str = payload.get('sub')
        if sub is None:
            raise credentials_exception
        token_data = TokenPayload(sub=sub)
    except JWTError:
        raise credentials_exception

    user = db.query(Users).filter(Users.id == token_data.sub).first()
    if user is None:
        raise credentials_exception
    return user


def get_employee_user(current_user: Users = Depends(get_current_user)) -> Users:
    if not user.is_employee(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user


from typing import Optional, List, Union, MutableMapping
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt

from app.models.users import Users
from app.core.config import settings
from app.core.security import verify_password

JWTPayloadMapping = MutableMapping[str, Union[datetime, str, bool, List[str], List[int]]]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{settings.API_V1_STR}/login')


def authenticate(*, email: str, password: str, db: Session) -> Optional[Users]:
    user = db.query(Users).filter(Users.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user


def _create_token(*, token_type: str, lifetime: timedelta, sub: int) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload['type'] = token_type
    payload['exp'] = expire
    payload['iat'] = datetime.utcnow()
    payload['sub'] = str(sub)
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


def create_access_token(*, sub: int) -> str:
    return _create_token(
        token_type='access_token',
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )

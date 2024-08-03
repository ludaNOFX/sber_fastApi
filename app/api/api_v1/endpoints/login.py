from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from app.api import deps
from app.schemas.token import Token
from app.core.auth import authenticate, create_access_token


router = APIRouter()


@router.post('/login', response_model=Token, status_code=200)
def login(*, db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    logged_user = authenticate(email=form_data.username, password=form_data.password, db=db)
    if not logged_user:
        raise HTTPException(
            status_code=400, detail='Incorrect username or password'
        )
    return {
        'access_token': create_access_token(sub=logged_user.id),
        'token_type': 'bearer'
    }

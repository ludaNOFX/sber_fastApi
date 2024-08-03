from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas.stack import Stacks, StackInDB
from app.schemas.users import Classes
from app.crud.crud_user import user
from app.crud.crud_stack import stack
from app.models.users import Users
from app.services.recruit import get_classes

router = APIRouter()


@router.get('/stacks', response_model=Stacks, status_code=200)
def get_stacks(*, db: Session = Depends(deps.get_db), current_user: Users = Depends(deps.get_employee_user)) -> Any:
    """Возвращает все стэки"""
    stacks = stack.get_multi(db)
    return {'results': stacks}


@router.post('/classes', response_model=Classes, status_code=200)
def get_users_classes(
        *,
        db: Session = Depends(deps.get_db),
        current_user: Users = Depends(deps.get_employee_user),
        stack_id: StackInDB
) -> Any:
    """Возвращает пользователей с определенным стэком и делит их на 3 класса"""
    users = user.get_multi_by_stack(db, stack_id.id)
    if not users:
        raise HTTPException(status_code=404, detail='Users not found')
    classes = get_classes(users)
    return classes

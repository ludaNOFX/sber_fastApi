from typing import Any, Union

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.users import Users
from app.schemas.users import UserCreate, UserUpdate, User
from app.schemas.quiz import Quiz
from app.schemas.rate import QuizResults
from app.schemas.exceptions import ErrorMessage
from app.api import deps
from app.crud.crud_user import user
from app import quiz
from app.services.rate import get_rate, overall_rate

router = APIRouter()


@router.post('/signup', response_model=User, status_code=201)
def create_user(*, db: Session = Depends(deps.get_db), user_in: UserCreate) -> Any:
    """Создает нового пользователя"""
    user_db = db.query(Users).filter(Users.email == user_in.email).first()
    if user_db:
        raise HTTPException(
            status_code=400,
            detail='The user with this email already exists in the system'
        )
    user_db = user.create(db=db, obj_in=user_in)
    return user_db


@router.put('/update', response_model=User, status_code=200)
def update_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: UserUpdate,
        current_user: Users = Depends(deps.get_current_user)
) -> Any:
    """Обновляет данные пользователя"""
    updated_user = user.update(db, db_obj=current_user, obj_in=user_in)
    return updated_user


@router.get('/hard_test', response_model=Union[Quiz, ErrorMessage], status_code=200)
def get_hard_test(
        *,
        current_user: Users = Depends(deps.get_current_user)
) -> Any:
    """Отправляет пользователю тест по его стэку"""
    hard_test = quiz.hard_skills.get(current_user.stack_id)
    if hard_test:
        return hard_test
    else:
        return ErrorMessage(message='Такой тест не найден')


@router.get('/soft_test', response_model=Union[Quiz, ErrorMessage], status_code=200)
def get_soft_test(
        *,
        current_user: Users = Depends(deps.get_current_user)
) -> Any:
    """Отправляет пользователю софт тест"""
    return quiz.soft_skills


@router.post('/get_hard_rate', response_model=User, status_code=200)
def get_hard_rate(
        *,
        db: Session = Depends(deps.get_db),
        current_user: Users = Depends(deps.get_current_user),
        rate_in: QuizResults
) -> Any:
    """Считает результаты теста и записывает их в бд"""
    rate = get_rate(rate_in)
    obj_in = UserUpdate(hard_rate=rate)
    updated_user = user.update(db, db_obj=current_user, obj_in=obj_in)
    return updated_user


@router.post('/get_soft_rate', response_model=User, status_code=200)
def get_soft_rate(
        *,
        db: Session = Depends(deps.get_db),
        current_user: Users = Depends(deps.get_current_user),
        rate_in: QuizResults
) -> Any:
    """Считает результаты теста и записывает их в бд"""
    rate = get_rate(rate_in)
    obj_in = UserUpdate(soft_rate=rate)
    updated_user = user.update(db, db_obj=current_user, obj_in=obj_in)
    return updated_user


@router.put('/get_overall_rate', response_model=User, status_code=200)
def get_overall_rate(
        *,
        db: Session = Depends(deps.get_db),
        current_user: Users = Depends(deps.get_current_user)
) -> Any:
    """Суммирует результаты тестов в общий балл и записывает в бд"""
    rate = overall_rate(current_user.hard_rate, current_user.soft_rate)
    obj_in = UserUpdate(rate=rate)
    updated_user = user.update(db, db_obj=current_user, obj_in=obj_in)
    return updated_user


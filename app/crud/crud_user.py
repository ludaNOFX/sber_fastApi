from typing import Any, Union, Dict, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.users import Users
from app.models.stack import Stack
from app.schemas.users import UserCreate, UserUpdate
from app.core.security import get_password_hash


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, email: str) -> Users:
        return db.query(Users).filter(Users.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> Users:
        create_data = obj_in.dict()
        create_data.pop('password')
        db_obj = Users(**create_data)
        db_obj.password_hash = get_password_hash(obj_in.password)
        db.add(db_obj)
        db.commit()
        return db_obj

    def update(
            self,
            db: Session,
            *,
            db_obj: Users,
            obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> Users:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if 'password' in update_data:
            hashed_password = get_password_hash(update_data['password'])
            del update_data['password']
            update_data['password_hash'] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_multi_by_stack(self, db: Session, stack: int) -> Users:
        return db.query(self.model).filter(self.model.stack_id == stack).all()

    def is_employee(self, current_user: Users) -> bool:
        return current_user.employee


user = CRUDUser(Users)

import logging
from sqlalchemy.orm import Session

from app.crud.crud_user import user
from app.crud.crud_stack import stack
from app.schemas.users import UserCreate
from app.schemas.stack import StackCreate
from app.db.base import Base
from app.core.config import settings

logger = logging.getLogger(__name__)

stacks = ['python/sql/pandas', 'java/spring/sql', 'javascript/vue/typescript']


def init_db(db: Session) -> None:
    if settings.FIRST_SUPERUSER:
        user_obj = user.get_by_email(db, settings.FIRST_SUPERUSER)
        if not user_obj:
            user_in = UserCreate(
                email=settings.FIRST_SUPERUSER,
                password=settings.FIRST_SUPERUSER_PW
            )
            user.create(db, obj_in=user_in)
        else:
            logger.warning(
                "Skipping creating superuser. User with email "
                f"{settings.FIRST_SUPERUSER} already exists. "
            )
    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_SUPERUSER needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_SUPERUSER=admin@api.coursemaker.io"
        )
    obj_stack = stack.get_multi(db)
    if not obj_stack:
        for s in stacks:
            stack_in = StackCreate(
                names=s
            )
            stack.create(db, obj_in=stack_in)
    else:
        logger.warning(
            'Stacks already exists in db'
        )

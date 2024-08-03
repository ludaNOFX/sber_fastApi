from typing import Any, Union, Dict, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.stack import Stack
from app.schemas.stack import StackCreate, StackUpdate


class CRUDStack(CRUDBase[Stack, StackCreate, StackUpdate]):
    ...


stack = CRUDStack(Stack)

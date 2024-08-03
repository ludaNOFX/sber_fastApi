from typing import List, Dict

from pydantic import BaseModel


class Question(BaseModel):
    question: str
    options: List[str]
    correct_answer: int


class Quiz(BaseModel):
    __root__: Dict[int, Question]


from typing import List, Dict

from pydantic import BaseModel


class Answer(BaseModel):
    correct_answer: int
    user_answer: int


class QuizResults(BaseModel):
    __root__: Dict[int, Answer]

from app.schemas.rate import QuizResults

from fastapi import HTTPException


def get_rate(data_in: QuizResults) -> float:
    data: dict = data_in.dict()
    rate = 0
    for res in data.values():
        for ans in res.values():
            if ans['correct_answer'] == ans['user_answer']:
                rate += 1
    return rate


def overall_rate(hard_rate: float, soft_rate: float) -> float:
    if not all([hard_rate, soft_rate]):
        raise HTTPException(
            status_code=400, detail="There is not hard_rate or soft_rate yet"
        )
    return hard_rate + soft_rate

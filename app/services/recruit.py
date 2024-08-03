from app.schemas.users import UsersInDB, User

from typing import Sequence


def get_classes(users_in: Sequence[User]) -> dict:
    high, mid, low = [], [], []
    for user in users_in:
        if user.rate >= 7:
            high.append(user)
        elif 3 <= user.rate < 7:
            mid.append(user)
        else:
            low.append(user)
    classes = dict(zip(['high', 'mid', 'low'], [high, mid, low]))
    return classes

from app.services.recruit import get_classes
from app.schemas.users import User

import pytest


@pytest.mark.parametrize(
    'data, expected_result',
    [
        (
            [
                {
                  "email": "user1@mail.com",
                  "name": "Leo",
                  "surname": "Messi",
                  "age": 30,
                  "rate": 9,
                  "stack_id": 1,
                  "id": 1
                },
                {
                    "email": "user2@mail.com",
                    "name": "Bob",
                    "surname": "Dylon",
                    "age": 300,
                    "rate": 1,
                    "stack_id": 1,
                    "id": 2
                },
                {
                    "email": "user3@mail.com",
                    "name": "Edic",
                    "surname": "Zaytsev",
                    "age": 26,
                    "rate": 6,
                    "stack_id": 1,
                    "id": 3
                }

            ],
            {
                'high': [
                    User(
                        email='user1@mail.com', name='Leo', surname='Messi', age=30,
                        city=None, tlg_link=None, rate=9.0, hard_rate=None, soft_rate=None,
                        employee=None, stack_id=1, id=1
                    )
                ],
                'mid': [
                    User(
                        email='user3@mail.com', name='Edic', surname='Zaytsev', age=26,
                        city=None, tlg_link=None, rate=6.0, hard_rate=None, soft_rate=None,
                        employee=None, stack_id=1, id=3
                    )
                ],
                'low': [
                    User(
                        email='user2@mail.com', name='Bob', surname='Dylon', age=300,
                        city=None, tlg_link=None, rate=1.0, hard_rate=None, soft_rate=None,
                        employee=None, stack_id=1, id=2
                    )
                ]
            }
        )
    ]
)
def test_get_classes(data, expected_result):
    obj_in = [User.parse_obj(i) for i in data]
    assert get_classes(obj_in) == expected_result

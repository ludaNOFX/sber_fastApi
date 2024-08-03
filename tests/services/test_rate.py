import pytest

from app.services.rate import get_rate, overall_rate
from app.schemas.rate import QuizResults


@pytest.mark.parametrize(
    'data, expected_result',
    [
        (
            {
                1: {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                2: {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                3: {
                    "correct_answer": 0,
                    "user_answer": 0
                }
            }, 3
        ),
        (
            {
                1: {
                    "correct_answer": 0,
                    "user_answer": 1
                },
                2: {
                    "correct_answer": 0,
                    "user_answer": 2
                },
                3: {
                    "correct_answer": 0,
                    "user_answer": 3
                }
            }, 0
        ),
        (
            {
                1: {
                    "correct_answer": 0,
                    "user_answer": 1
                },
                2: {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                3: {
                    "correct_answer": 0,
                    "user_answer": 0
                }
            }, 2
        )

    ]
)
def test_get_rate(data, expected_result):
    data_obj = QuizResults.parse_obj(data)
    res = get_rate(data_obj)
    assert res == expected_result


@pytest.mark.parametrize('hard_rate, soft_rate, expected_result', [(9, 9, 18)])
def test_get_overall_rate(hard_rate, soft_rate, expected_result):
    assert overall_rate(hard_rate, soft_rate) == expected_result

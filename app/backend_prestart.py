import logging

from tenacity import before_log, after_log, retry, wait_fixed, stop_after_attempt

from app.db.session import SessionLocal

from sqlalchemy import text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 10
wait_seconds = 5


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN)
)
def init() -> None:
    """декоратор retry позволяет настроить количество выполнений кода при неудачной попытке"""
    try:
        db = SessionLocal()
        db.execute(text('SELECT 1'))
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    """В этом скрипте я проверяю работает ли бд. Делаю легкий запрос к базе. В случае ошибке
    повторяю попытки заданное количество раз"""
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == '__main__':
    main()

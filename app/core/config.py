from pydantic import BaseSettings, EmailStr
import os


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str
    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PW: str
    JWT_SECRET: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    TEST_USER_EMAIL: EmailStr
    TEST_USER_PW: str

    class Config:
        env_file = f'{os.path.dirname(os.path.abspath(__file__))}/../../.env'


settings = Settings(
    _env_file_encoding='utf-8'
)

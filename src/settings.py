from pydantic import BaseSettings, RedisDsn
from fastapi.templating import Jinja2Templates


class Settings(BaseSettings):
    host: str
    port: int
    redis_url: RedisDsn
    reload: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
templates = Jinja2Templates(directory='templates')

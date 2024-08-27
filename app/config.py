from pydantic import BaseSettings
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./app/templates")


class Settings(BaseSettings):
    mongoDB_url:str
    db:str
    collection:str
    users_collection:str
    class Config:
        env_file=".env"

settings = Settings()
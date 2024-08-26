from pydantic import BaseSettings

class Settings(BaseSettings):
    mongoDB_url:str
    db:str
    collection:str
    class Config:
        env_file=".env"

settings = Settings()
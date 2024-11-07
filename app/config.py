from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongodb_url: str
    database_name: str
    secret_key: str

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    return Settings() 
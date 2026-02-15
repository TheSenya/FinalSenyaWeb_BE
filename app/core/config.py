from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

# BaseSettings as a contract between your code and the outside world
# While a normal Pydantic BaseModel validates data you pass into it (like a JSON request),
# BaseSettings reaches out and pulls data from your environment automatically.

# BaseSettings populates itself with the data found in the system environemt and the .env file
# The order of precedence is:
# 1. Environment variables
# 2. .env file
# 3. Default values

# Base settigs also performs Type Casting
# For example, if you have a variable that is a string in the environment,
# but you define it as an int in your class, BaseSettings will try to convert it to an int.
# If it fails, it will raise a ValueError.


class Settings(BaseSettings):
    # Project Info
    PROJECT_NAME: str = "senyaweb-be"
    PROJECT_VERSION: str = "0.1.0"
    DEBUG: bool = False
    ENV: Literal["dev", "prod", "test"] = "dev"

    # Database
    # TODO: Add database URL
    # DATABASE_URL: str

    # API
    API_PREFIX: str = "/api"
    API_VERSION: str = "v1"

    # Settings Config
    # This tells BaseSettings where to look for the environment variables
    # env_file: The path to the .env file
    # env_file_encoding: The encoding of the .env file
    # extra: What to do with extra environment variables
    #        - ignore: Ignore extra environment variables
    #        - raise: Raise an error if extra environment variables are found
    #        - allow: Allow extra environment variables
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

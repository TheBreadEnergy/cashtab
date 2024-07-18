from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.utils import get_from_pyproject_toml

name, version, description = get_from_pyproject_toml()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", env_file=".env")

    project_name: str = Field(
        name,
        alias="PROJECT_NAME",
        env="PROJECT_NAME",
    )
    description: str = Field(
        description,
        alias="DESCRIPTION",
        env="DESCRIPTION",
    )
    version: str = Field(version, alias="VERSION", env="VERSION")
    debug: bool = Field(False, alias="DEBUG", env="DEBUG")

    host: str = Field('localhost', alias="HOST", env="HOST")

    port: int = Field(8000, alias="PORT", env="PORT")


settings = Settings()

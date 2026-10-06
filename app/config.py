from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "Project API"
    app_env: str = "development"


settings = Settings()
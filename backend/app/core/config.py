from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "World Tourism API"
    app_env: str = "development"
    debug: bool = True

    database_url: str

    frontend_url: str = "http://localhost:5173"

    duffel_api_key: str = "duffel_test_VSUNr-qoyToKC18WQ_9rV-eQ4mJrQADETnaNF1-n9EG"
    duffel_base_url: str = "https://api.duffel.com"

    duffel_success_url: str = "https://disclosure-brother-reward-beatles.trycloudflare.com/booking/success"
    duffel_failure_url: str = "https://disclosure-brother-reward-beatles.trycloudflare.com/booking/failure"
    duffel_abandonment_url: str = "https://disclosure-brother-reward-beatles.trycloudflare.com/booking/abandoned"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()

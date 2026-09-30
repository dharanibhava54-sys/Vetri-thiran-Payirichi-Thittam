import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = "FitBuddy - AI Fitness Plan Generator"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")


settings = Settings()
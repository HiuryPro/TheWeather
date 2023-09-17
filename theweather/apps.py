from django.apps import AppConfig
from dotenv import load_dotenv


class TheWeatherConfig(AppConfig):
    load_dotenv(dotenv_path="./.env")
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theweather'

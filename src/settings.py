from enum import Enum
from decouple import config


class Environment(Enum):
    PRODUCTION = 'production'
    DEVELOPMENT = 'development'


ENVIRONMENT = Environment(config('ENVIRONMENT'))
PROJECT = config('PROJECT')
MICROSOFT_STORE_URL = config('MICROSOFT_STORE_URL')
NINTENDO_STORE_URL = config('NINTENDO_STORE_URL')
STEAM_URL = config('STEAM_URL')

from uuid import uuid4
from src.services.api_request import api_request
from src.utils.get_mocks import get_mocks
from src.settings import Environment, ENVIRONMENT, MICROSOFT_STORE_URL, NINTENDO_STORE_URL, STEAM_URL


async def api_request_or_mocks():
    return await api_request([
        MICROSOFT_STORE_URL,
        NINTENDO_STORE_URL,
        STEAM_URL
    ]) if ENVIRONMENT == Environment.PRODUCTION else get_mocks('./src/mocks')


async def short_description():
    request = await api_request_or_mocks()

    return [{
        'uuid': uuid4(),
        'name': req.get('name') or req.get('game-name') or req.get('title'),
        'short_description': req.get('short-game-description') or req.get('description') or req.get('shortDescription')
    } for req in request]


async def long_description(params):
    request = await api_request_or_mocks()
    result_list = [{
        'uuid': uuid4(),
        'name': req.get('name') or req.get('game-name') or req.get('title'),
        'long_description': req.get('longgest-game-description') or req.get('long-term-description') or req.get('longDescription')
    } for req in request]

    return [res for res in result_list if res['name'] == params['name']][0]

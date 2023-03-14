from fastapi import FastAPI
from src.utils.exec_task import exec_task
from src.functions import game

app = FastAPI()


@app.get('/games')
async def game_short_description():
    """
        Irá retornar uma lista de objetos GameShortDescription em JSON
    """
    return await exec_task(game.short_description)


@app.get('/games/{name}')
async def game_long_description(name):
    """
        Irá retornar um objeto GameLongDescription em JSON
    """
    return await exec_task(game.long_description, {'name': name})

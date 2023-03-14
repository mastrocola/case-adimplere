from fastapi import HTTPException


def not_empty(value: str):
    if not value:
        raise HTTPException(status_code=400, detail='The parameter must be specified')

    return value

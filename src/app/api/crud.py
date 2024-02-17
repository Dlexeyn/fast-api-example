from app.db import heroes, database
from app.model import HeroSchema


async def post(payload: HeroSchema):
    query = heroes.insert().values(name=payload.name, description=payload.description)
    return await database.execute(query=query)


async def get(id: int):
    query = heroes.select().where(id == heroes.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = heroes.select()
    return database.fetch_all(query=query)
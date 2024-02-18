import logging

from app.db import heroes, database
from app.model.Hero import HeroSchema


async def post(payload: HeroSchema):
    query = heroes.insert().values(name=payload.name, description=payload.description)
    return await database.execute(query=query)


async def get(id: int):
    query = heroes.select().where(id == heroes.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = heroes.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: HeroSchema):
    query = (
        heroes
        .update()
        .where(id == heroes.c.id)
        .values(name=payload.name, description=payload.description)
        .returning(heroes.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = heroes.delete().where(id == heroes.c.id)
    return await database.execute(query=query)

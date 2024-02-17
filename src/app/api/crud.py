from app.api.db import heroes, database
from app.model import HeroSchema


async def post(payload: HeroSchema):
    query = heroes.insert().values(name=payload.name, description=payload.description)
    return await database.execute(query=query)

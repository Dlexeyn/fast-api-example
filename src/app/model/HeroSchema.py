from pydantic import BaseModel


class HeroSchema(BaseModel):
    name: str
    description: str


class HeroDB(HeroSchema):
    id: int

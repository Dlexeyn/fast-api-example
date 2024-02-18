from pydantic import BaseModel, Field


class HeroSchema(BaseModel):
    name: str = Field(..., min_lenght=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=80)


class HeroDB(HeroSchema):
    id: int

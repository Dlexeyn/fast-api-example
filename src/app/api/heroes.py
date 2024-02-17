from fastapi import APIRouter

from app.api import crud
from app.model.HeroSchema import HeroDB, HeroSchema

router = APIRouter()


@router.post("/", response_model=HeroDB, status_code=201)
async def create_hero(payload: HeroSchema):
    hero_id = await crud.post(payload)
    res_object = {
        "id": hero_id,
        "name": payload.name,
        "description": payload.description
    }
    return res_object

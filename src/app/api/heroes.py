from typing import List

from fastapi import APIRouter, HTTPException

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


@router.get("/{id}", response_model=HeroDB)
async def get_hero(id: int):
    hero = await crud.get(id)
    if not hero:
        raise HTTPException(status_code=404, detail=f"Hero with {id} not found")
    return hero


@router.get("/", response_model=List[HeroDB])
async def get_all():
    return await crud.get_all()

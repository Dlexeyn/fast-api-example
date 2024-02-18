import logging
from typing import List
from fastapi import APIRouter, HTTPException, Path
from app.api import crud
from app.model.Hero import HeroDB, HeroSchema

router = APIRouter()
logger = logging.getLogger(__name__)


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
async def get_hero(id: int = Path(..., gt=0)):
    hero = await crud.get(id)
    if not hero:
        raise HTTPException(status_code=404, detail=f"Hero with id={id} not found")
    return hero


@router.get("/", response_model=List[HeroDB])
async def get_all():
    heroes = await crud.get_all()
    return heroes


@router.put("/{id}", response_model=HeroDB)
async def update_hero(payload: HeroSchema, id: int = Path(..., gt=0)):
    hero = await crud.get(id)
    if not hero:
        raise HTTPException(status_code=404, detail=f"Hero with id={id} not found")

    hero_id = await crud.put(id, payload)

    res_object = {
        "id": hero_id,
        "name": payload.name,
        "description": payload.description
    }
    return res_object


@router.delete("/{id}")
async def delete_hero(id: int = Path(..., gt=0)):
    hero = await crud.get(id)
    if not hero:
        raise HTTPException(status_code=404, detail=f"Hero with id={id} not found")

    await crud.delete(id)

    return {"status": f"Hero with id={id} deleted."}

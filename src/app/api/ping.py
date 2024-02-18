from fastapi import APIRouter
import logging

router = APIRouter()


@router.get("/ping")
async def pong():
    logging.info("ping")
    return {"ping": "pong!"}

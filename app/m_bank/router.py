from fastapi import APIRouter

from app.m_bank.parser import parser

router = APIRouter()


@router.post("/load_mbank")
async def read_root(data: str):
    await parser(data)

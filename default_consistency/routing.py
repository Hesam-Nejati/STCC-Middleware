#deafult_consistency/routing.py
from fastapi import APIRouter, Request
from middleware.consistency import handle_stcc_logic

router = APIRouter()

@router.post("/execute")
async def execute_operation(request: Request):
    data = await request.json()
    result = handle_stcc_logic(data)
    return result

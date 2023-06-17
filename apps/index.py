from fastapi import APIRouter

index_router = APIRouter()

@index_router.post("/")
async def test():
    return {"test": "12321312"}
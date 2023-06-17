from fastapi import APIRouter

index_router = APIRouter()

@index_router.get("/")
async def test():
    return {"test": "12321312"}
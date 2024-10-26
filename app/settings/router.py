from fastapi import APIRouter


instance_router = APIRouter(tags=['Base'])

@instance_router.get("/")
async def root():
    return {"message": "Hello World"}

@instance_router.get("/auth")
async def auth():
    return {"message": "Auth"}
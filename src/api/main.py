from fastapi import  FastAPI
from src.api.routers import work_order_router

app = FastAPI()
app.include_router(work_order_router.router)


@app.get("/")
async def root():
    return {"message": "Welcome to root of Service Order Supply API!"}
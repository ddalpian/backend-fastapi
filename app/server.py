from .routers import items_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(items_router)

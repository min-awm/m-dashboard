from contextlib import asynccontextmanager

from auth.api import router as auth_router
from chat.api import router as chat_router
from core.middleware import Middleware
from core.mongodb import init_db
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="M-dashboard API",
    version="1.0.0",
)

app.add_middleware(Middleware)
app.include_router(auth_router)
app.include_router(chat_router)

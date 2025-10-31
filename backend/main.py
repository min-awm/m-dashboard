from contextlib import asynccontextmanager

from auth.api import router as auth_router
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


app.include_router(auth_router)

@app.middleware("http")
async def jwt_middleware(request: Request, call_next):
    # Không validate JWT cho route public (ví dụ /login)
    if request.url.path in ["/login", "/docs", "/openapi.json"]:
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if auth_header is None or not auth_header.startswith("Bearer "):
        return JSONResponse(status_code=401, content={"detail": "Missing or invalid Authorization header"})

    token = auth_header.split(" ")[1]
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        request.state.user = payload  # lưu thông tin user vào request.state
    except PyJWTError:
        return JSONResponse(status_code=401, content={"detail": "Invalid token"})
    
    response = await call_next(request)
    return response
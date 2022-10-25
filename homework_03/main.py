from fastapi import FastAPI

from api.items import router as items_router
from api.users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/ping/", status_code=200)
async def root():
    return {"message": "pong"}


@app.get("/hello/", status_code=200)
def hello():
    return {"Hello": "world!"}

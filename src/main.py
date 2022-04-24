from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from src.settings import settings
from src.router import router
from src.utils import get_redis_client

app = FastAPI()
app.include_router(router)
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.on_event('startup')
async def startup():
    app.state.redis = get_redis_client()


@app.on_event('shutdown')
async def shutdown():
    await app.state.redis.close()


if __name__ == '__main__':
    uvicorn.run('src.main:app', host=settings.host, port=settings.port, reload=settings.reload)

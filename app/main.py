from fastapi import FastAPI, APIRouter

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(title='Hiring_service')

app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8001, log_level='debug')

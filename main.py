from routers import products
from routers import users

import pip

try:
    from pydantic import BaseModel

except ImportError:
    pip.main(['install', 'pydantic'])
try:
    from fastapi import (
        FastAPI,
        HTTPException,
        staticfiles
    )

except ImportError:
    pip.main(['install', 'fastapi'])





app = FastAPI()


#   Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount('/static', staticfiles.StaticFiles(directory='static'), name = 'static')


#   Images
#   http://127.0.0.1:8000/static/img/P001.png
#   http://127.0.0.1:8000/static/img/P002.png


@app.get("/")
async def root():
    return 'fastAPI'


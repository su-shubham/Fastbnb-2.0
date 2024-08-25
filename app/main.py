from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import routes

app = FastAPI()
app.include_router(routes.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")






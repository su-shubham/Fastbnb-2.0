from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import routes,properties

app = FastAPI()
app.include_router(routes.router)
app.include_router(properties.property)

app.mount("/static", StaticFiles(directory="app/static"), name="static")






from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import rent_router,property_router
from app.auth import users_router

app = FastAPI()
app.include_router(property_router)
app.include_router(rent_router)
app.include_router(users_router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")






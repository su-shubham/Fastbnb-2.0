from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request
from app.config import templates

rent = APIRouter(
    prefix="/rent",
    tags=["rent"],
)

@rent.get("/",response_class=HTMLResponse)
async def show_data(request: Request):
    return templates.TemplateResponse("rent.html", {"request": request})
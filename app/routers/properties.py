from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter
from app.config import templates
from ..repo import get_individual_info, confirm_book, search_data, get_data

property = APIRouter(
    prefix="",
    tags=["properties"],
)


@property.get("/", response_class=HTMLResponse)
async def home(request: Request):
    response = await get_data()
    print(get_data)
    if response:
        return templates.TemplateResponse(
            "index.html", {"request": request, "response": response}
        )
    else:
        print("Not found")


@property.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("./components/login.html", {"request": request})


@property.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(
        "./components/register.html", {"request": request}
    )


@property.get("/search")
async def search(query: str):
    search_results = await search_data(query)
    return search_results


@property.get("/listing/{id}", response_class=HTMLResponse)
async def listing(request: Request, id):
    get_individual_data = await get_individual_info(id)
    if get_individual_data:
        return templates.TemplateResponse(
            "listing.html", {"request": request, "property": get_individual_data}
        )
    else:
        print("Not found")

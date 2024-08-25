from fastapi import  Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter
from starlette.templating import Jinja2Templates
from ..database import (
    get_data,
    get_individual_info, 
    confirm_book,
    search_data
)

templates = Jinja2Templates(directory="./app/templates")

router=APIRouter()

@router.get('/',response_class=HTMLResponse)
async def home(request:Request):
    response = await get_data()
    if response:
        return templates.TemplateResponse("index.html",{"request":request,"response":response})
    else:
        print("Not found")

@router.get("/login",response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse("./components/login.html",{"request":request})

@router.get("/register",response_class=HTMLResponse)
async def register(request:Request):
    return templates.TemplateResponse("./components/register.html",{"request":request})

@router.get("/search")
async def search(query:str):
    search_results = await search_data(query)
    return search_results
   
@router.get('/listing/{id}',response_class=HTMLResponse)
async def listing(request:Request,id):
    get_individual_data = await get_individual_info(id)
    if get_individual_data:
        return templates.TemplateResponse("listing.html",{"request":request,"property":get_individual_data})
    else:
        print("Not found")

@router.get('/confirmation/{id}',response_class=HTMLResponse)
async def confirm(request:Request,id):
    get_confirm_data = await confirm_book(id)
    if get_confirm_data.inserted_id:
        return templates.TemplateResponse("confirmation.html",{"request":request,'confirmation':get_confirm_data})
    else:
        print("Not found")
    


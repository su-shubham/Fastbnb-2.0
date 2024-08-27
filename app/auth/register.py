from app.auth.utils import get_password_hash, verify_user_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import HTTPException, Depends, APIRouter
from app.config import settings
from app.models import User

users = APIRouter(
    prefix="/users",
    tags=["users"],
)


@users.post("/register")
async def register_users(user: User):
    user_data = settings.users_collection.find_one({"email": user.email})
    if user_data:
        raise HTTPException(status_code=400, detail="User already registered")

    hashed_password = get_password_hash(user.password)
    user_dict = user.dict() 
    user_dict["password"] = hashed_password
    results = settings.user_collection.insert_one(user_dict)
    print(f"User inserted with id: {results.inserted_id}")
    print(results)
    return {"message": "User registered successfully"}


@users.post("/login")
async def login_users(form_data: OAuth2PasswordRequestForm = Depends()):
    user_data = settings.users_collection.find_one({"email": form_data.username})
    if not user_data or not verify_user_password(
        form_data.password, user_data["password"]
    ):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user_data["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

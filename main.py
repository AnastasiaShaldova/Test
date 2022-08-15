from fastapi import FastAPI

from app.pkg.models import User
from app.pkg.user import users_get, get_user_by_name

app = FastAPI()


@app.post("/users")
async def save_user(user_details: User):
    return {'name': user_details.name, 'gender': user_details.gender}


@app.get("/users_get")
async def users_list():
    return await users_get()


@app.post("/user_get_name")
async def user_get_name(user_details: str):
    return get_user_by_name(user_details)



import pip

try:
    from pydantic import BaseModel

except ImportError:
    pip.main(['install', 'pydantic'])
try:
    from fastapi import (
        APIRouter,
        HTTPException
    )

except ImportError:
    pip.main(['install', 'fastapi'])





router = APIRouter()



class User(BaseModel):
    id : int
    username : str
    password : str


users_list = [
    User(id = 1, username = "admin", password = "admin"),
    User(id = 2, username = "user1", password = "user1"),
    User(id = 3, username = "user2", password = "user2"),
    User(id = 4, username = "user3", password = "user3"),
    User(id = 5, username = "user4", password = "user4"),
    User(id = 6, username = "user5", password = "user5")
]



@router.get("/user/")
async def users():
    return users_list

@router.get("/search/user/{id}")
async def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    
    try:
        return list(users)
    
    except Exception as exception:
        return {'exception': exception}


@router.post("/add/user/", status_code = 201)
async def add_user(user: User):
    
    if type(search_user(user.id)) is User:
        HTTPException(status_code = 404, detail = "User already exists")

    else:
        return users_list.append(user)



@router.put("/update/user/{id}")
async def update_user(user: User):
    found = False
    
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {'message': 'User not found'}

@router.delete("/delete/user/{id}")
async def delete_user(id: int):
    found = False
    
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {'message': 'User not found'}
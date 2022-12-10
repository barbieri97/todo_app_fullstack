from pydantic import BaseModel
from typing import List


class Login(BaseModel):
    username: str
    password: str

class Item(BaseModel):
    name: str
    done: bool = False

    class Config:
        orm_mode = True

class ShowItem(Item):
    id: int

class User(BaseModel):
    username: str
    email: str
    password: str

class ShowUser(BaseModel):
    username: str
    email: str
    todos: List[ShowItem]
    
    class Config:
        orm_mode = True
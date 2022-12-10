from fastapi import FastAPI
from todo_list.routers import auth, user
from todo_list import database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(user.router)

database.Base.metadata.create_all(bind=database.engine)

@app.get('/')
def index():
    return {'detail': 'you are in the index view'}
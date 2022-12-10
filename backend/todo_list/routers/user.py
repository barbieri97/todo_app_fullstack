from fastapi import APIRouter, Depends, status
from .. import schemas, models, oauth2, hash
from ..crud import user
from ..database import get_db
from sqlalchemy.orm import Session



router = APIRouter(
    prefix='/user',
    tags=['user']
)



@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/me', response_model=schemas.ShowUser)
async def get_user(current_user: schemas.User = Depends(oauth2.get_current_user),  db: Session = Depends(get_db)):
    return user.get_user(current_user, db)

@router.post('/me/todo', response_model=schemas.Item, status_code=status.HTTP_201_CREATED)
async def create_todo(request: schemas.Item,  current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return user.create_todo(request, current_user, db)

@router.delete('/me/{todo_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_todo(todo_id, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return user.delete_todo(todo_id, current_user, db)
from .. import schemas, models, hash
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def create_user(request: schemas.User, db: Session):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if user:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='username alredy exists')
    request.password = hash.Hash.encrypt(request.password)
    db_user = models.User(**request.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(current_user: schemas.User, db: Session):
    user = db.query(models.User).filter(models.User.username == current_user.get('username')).first()
    return schemas.ShowUser(username=user.username, email=user.email, todos=user.todos)

def create_todo(request: schemas.Item, current_user: schemas.User, db: Session):
    user = db.query(models.User).filter(models.User.username == current_user.get('username')).first()
    user_id = user.id

    todo = models.Item(owner_id=user_id, **request.dict())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(id: int, current_user: schemas.User, db: Session):
    """ Deleta o todo do usuário baseado no seu id  """
    todo = db.query(models.Item).filter(models.Item.owner_id == current_user.get('user_id'), models.Item.id == id).delete()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='todo not found')
    db.commit()
    return {'detail': 'success'}

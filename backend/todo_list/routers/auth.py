from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, token, database, hash
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['auth']
)



@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    # Busca no banco de dados o primeiro usuario com o username da requisição
    user = db.query(models.User).filter(models.User.username == request.username).first()
    
    #Verifica se há um usuario com o username enviado
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='username or password invalid')
    #Verifica se a senha passada é igual a senha salva no banco de dados
    if not hash.Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='username or password invalid')

    #Cria os dados para criar o JWT
    data = {"email": user.email, 'username': user.username, 'user_id': user.id}
    
    # Se passar nas verificações cria o JWT e retorna
    access_token = token.create_token(data) 
    return {"access_token": access_token, "token_type": "Bearer"}
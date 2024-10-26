from fastapi import APIRouter, HTTPException, status
from services.validation.InRegisterUser import InRegisterUser
from services.authorization.AuthorizationServices import Authorization
from models.UserModels import User

instance_router = APIRouter(prefix="/auth", tags=['Auth'])

@instance_router.post("/register/")
async def register_user(user_data: InRegisterUser) -> dict:
    user = await User.find_one_or_none(login=user_data.login)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Пользователь уже существует')
    user_dict = user_data.dict()
    user_dict['password'] = Authorization.get_password_hash(user_data.password)
    await User.add(**user_dict)
    return {'message': f'Вы успешно зарегистрированы!'}
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from settings.AppSettings import Settings
from jose import jwt
class Authorization:

    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    settings = Settings()
    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return cls.pwd_context.verify(plain_password, hashed_password)
    
    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.pwd_context.hash(password)
    
    @classmethod
    def create_access_token(cls, data: dict, expires_delta: int = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, cls.settings.SECRET_KEY, algorithm=cls.settings.ALGORITHM)
        return encoded_jwt
import os
from dotenv import load_dotenv
from fastapi import Security, HTTPException, status, Depends
from fastapi.security.api_key import APIKeyHeader
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from typing import cast

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "X-API-KEY"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY and API_KEY is not None:
        return api_key_header

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Acesso negado: API Key inválida ou ambiente não configurado"
    )

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashHelper:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Compara a senha digitada com o hash do banco"""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        """Gera um hash seguro a partir da senha pura"""
        return pwd_context.hash(password)


# CONFIGURAÇÕES (Pode mudar a SECRET_KEY para o que quiser)
SECRET_KEY = "sua_chave_secreta_muito_segura_e_longa"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(data: dict):
    """Gera o token JWT assinado"""
    to_encode = data.copy()

    # Define a expiração (Ex: agora + 30 minutos)
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    # O jwt.encode é quem faz a mágica de criar o token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email = cast(str, payload.get("sub"))

        if email is None:
            raise credentials_exception

        return email
    except JWTError:
        raise credentials_exception

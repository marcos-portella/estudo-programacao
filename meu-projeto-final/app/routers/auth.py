from fastapi import APIRouter, Depends
from mysql.connector.abstracts import MySQLConnectionAbstract
from app.models.users import UserCreate
from app.services.auth_service import AuthService
from app.dependencies.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", summary="Registrar novo administrador")
def create_user(
    user_data: UserCreate, db: MySQLConnectionAbstract = Depends(get_db),
    user_email: str = Depends(get_current_user)
):
    """
    Cria um novo usuário no sistema.
    Esta descrição detalhada aparece logo abaixo do título quando a rota é
    expandida. Usar como exemplo.
    """
    return AuthService.create_user(user_data, db, user_email)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: MySQLConnectionAbstract = Depends(get_db)
):
    # O OAuth2PasswordRequestForm espera 'username' (que será o email) e
    # 'password'
    return AuthService.authenticate_user(
        db, form_data.username, form_data.password
    )

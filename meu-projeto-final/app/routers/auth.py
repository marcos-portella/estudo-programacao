from fastapi import APIRouter, Depends
from mysql.connector.abstracts import MySQLConnectionAbstract
from app.models.users import UserCreate
from app.services.auth_service import AuthService
from app.dependencies.database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def create_user(
    user_data: UserCreate, db: MySQLConnectionAbstract = Depends(get_db)
):
    return AuthService.create_user(user_data, db)


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

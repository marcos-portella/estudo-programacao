from mysql.connector.abstracts import MySQLConnectionAbstract
from app.models.users import UserCreate
from app.dependencies.auth import HashHelper, create_access_token
from fastapi import HTTPException
from typing import Any, Dict, cast


class AuthService:
    @staticmethod
    def create_user(
        user_data: UserCreate, db: MySQLConnectionAbstract, user_email: str
    ):
        cursor = db.cursor(dictionary=True)

        # 1. Verificar se o e-mail já existe
        cursor.execute(
            "SELECT id FROM users WHERE email = %s", (user_data.email,)
        )
        if cursor.fetchone():
            cursor.close()
            raise HTTPException(status_code=400, detail="E-mail já cadastrado")

        # 2. Criptografar a senha (HASHING)
        print(f"DEBUG: Senha recebida -> {user_data.password}")
        hashed_pwd = HashHelper.get_password_hash(user_data.password)

        # 3. Salvar no banco
        sql = """INSERT INTO users (email, hashed_password, full_name)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (user_data.email, hashed_pwd, user_data.full_name))

        db.commit()
        new_id = cursor.lastrowid
        cursor.close()

        return {
            "id": new_id, "email": user_data.email,
            "message": "Usuário criado com sucesso",
            "created_by": user_email
        }

    @staticmethod
    def authenticate_user(
        db: MySQLConnectionAbstract, email: str, password: str
    ):
        # Usamos dictionary=True, mas precisamos avisar o Mypy disso
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        # Cast diz ao Mypy: "Confia em mim, isso aqui é um dicionário ou None"
        user = cast(Dict[str, Any], cursor.fetchone())
        cursor.close()

        # 2. Se não achar ou a senha estiver errada:
        if not user:
            raise HTTPException(
                status_code=401, detail="E-mail ou senha incorretos"
            )

        # Aqui usamos str() ou cast para garantir que o valor enviado é string
        hashed_password = cast(str, user["hashed_password"])
        user_email_code = cast(str, user["email"])

        if not HashHelper.verify_password(password, hashed_password):
            raise HTTPException(
                status_code=401, detail="E-mail ou senha incorretos"
            )

        # 3. Se deu tudo certo, gera o Token
        token = create_access_token(data={"sub": user_email_code})

        return {"access_token": token, "token_type": "bearer"}

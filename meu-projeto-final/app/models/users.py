from pydantic import BaseModel, EmailStr, ConfigDict, Field


class UserCreate(BaseModel):
    email: EmailStr = Field(
        ..., description="Endereço de e-mail único do usuário"
    )
    password: str = Field(
        ..., min_length=6, description="Senha de acesso (mínimo 6 caracteres)"
    )
    full_name: str = Field(
        ..., description="Nome completo do administrador"
    )


class UserResponse(BaseModel):
    id: int
    email: EmailStr = Field(
        ..., description="Endereço de e-mail único do usuário"
    )
    full_name: str = Field(
        ..., description="Nome completo do administrador"
    )

    model_config = ConfigDict(from_attributes=True)

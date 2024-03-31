from pydantic import BaseModel
# Валидатор для регистрации
class RegisterValidator(BaseModel):
    user_name: str
    surname: str
    phone_number: int
    city: str
    password: int
# Валидатор для логина
class EditUserValidator(BaseModel):
    user_id: int
    edit_info: str
    new_info: str
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import date
from enum import Enum

class CategoryEnum(str, Enum):
    food = "food"
    entertainment = "entertainment"
    health = "health"
    education = "education"
    others = "others"

class Sales(BaseModel):
    '''Modelo de dados para vendas
        Argumentos:
            email (str): Email do comprador
            date (datetime): Data da compra
            value (float): Valor da compra
            amount (float): Quantidade de itens
            product (str): Nome do item
            category (str): Categoria da compra
    '''

    email: EmailStr
    date: date
    value: PositiveFloat
    amount: PositiveInt
    product: str
    category: CategoryEnum

    # Validacao de categoria
    @field_validator('category')
    def validate_category(cls, error):
        if error not in CategoryEnum:
            raise ValueError('Invalid category')
        return error
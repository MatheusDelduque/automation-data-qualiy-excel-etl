import pytest
from datetime import datetime
from src.contract import Sales
from pydantic import ValidationError

# Testes com dados validos
def test_valid_data():
    valid_data = {
        'email': 'qNt9h@example.com',
        'date': datetime.now(),
        'value': 100.0,
        'amount': 10,
        'product': 'Banana',
        'category': 'food'
    }

    sales = Sales(**valid_data)

    assert sales.email == valid_data['email']
    assert sales.date == valid_data['date']
    assert sales.value == valid_data['value']
    assert sales.amount == valid_data['amount']
    assert sales.product == valid_data['product']
    assert sales.category == valid_data['category']

def test_invalid_data():
    invalid_data = {
        'email': 'qNt9h@example.com',
        'date': datetime.now(),
        'value': -100.0,
        'amount': -10,
        'product': 'Banana',
        'category': 'invalid'
    }

    with pytest.raises(ValidationError):
        Sales(**invalid_data)

def test_category_validation():
    invalid_data = {
        'email': 'qNt9h@example.com',
        'date': datetime.now(),
        'value': 100.0,
        'amount': 10,
        'product': 'Banana',
        'category': 'invalid'
    }

    with pytest.raises(ValidationError):
        Sales(**invalid_data)
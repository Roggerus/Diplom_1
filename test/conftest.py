import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 50
    return bun

@pytest.fixture
def mock_ingredient_factory():
    def _create(name="Test Ingredient", price=50, ing_type=INGREDIENT_TYPE_SAUCE):
        ingredient = Mock()
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        ingredient.get_type.return_value = ing_type
        return ingredient
    return _create

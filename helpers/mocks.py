from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

def create_mock_ingredient(
    name="Test Ingredient",
    price=50,
    ing_type=INGREDIENT_TYPE_SAUCE
):
    ingredient = Mock()
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price
    ingredient.get_type.return_value = ing_type
    return ingredient

import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient_factory):
        ingredient = mock_ingredient_factory()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger, mock_ingredient_factory):
        ingredient = mock_ingredient_factory()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_invalid_index(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient(self, burger, mock_ingredient_factory):
        ing1 = mock_ingredient_factory(name="A")
        ing2 = mock_ingredient_factory(name="B")
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing1

    def test_move_ingredient_invalid_index(self, burger, mock_ingredient_factory):
        ingredient = mock_ingredient_factory()
        burger.add_ingredient(ingredient)
        with pytest.raises(IndexError):
            burger.move_ingredient(10, 0)

    def test_move_ingredient_empty_list(self, burger):
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 0)

    @pytest.mark.parametrize("bun_price, ingredients_prices, expected_price", [
        (100, [50, 50], 300),
        (50, [20, 30, 40], 190),
        (0, [], 0),
    ])
    def test_get_price(self, burger, mock_bun, mock_ingredient_factory, bun_price, ingredients_prices, expected_price):
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredients_prices:
            ingredient = mock_ingredient_factory(price=price)
            burger.add_ingredient(ingredient)
        assert burger.get_price() == expected_price

    def test_get_price_no_bun(self, burger, mock_ingredient_factory):
        ingredient = mock_ingredient_factory()
        burger.add_ingredient(ingredient)
        with pytest.raises(AttributeError):
            burger.get_price()

    @pytest.mark.parametrize("bun_name, ingredient_data, expected_receipt", [
        ("Black Bun", [(INGREDIENT_TYPE_SAUCE, "Ketchup", 50)], "(==== Black Bun ====)\n= sauce Ketchup =\n(==== Black Bun ====)\n\nPrice: 150"),
        ("White Bun", [(INGREDIENT_TYPE_FILLING, "Cheese", 25), (INGREDIENT_TYPE_SAUCE, "Mayo", 25)], "(==== White Bun ====)\n= filling Cheese =\n= sauce Mayo =\n(==== White Bun ====)\n\nPrice: 150"),
    ])
    def test_get_receipt(self, burger, mock_bun, mock_ingredient_factory, bun_name, ingredient_data, expected_receipt):
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)
        for ing_type, name, price in ingredient_data:
            ingredient = mock_ingredient_factory(name=name, price=price, ing_type=ing_type)
            burger.add_ingredient(ingredient)
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_no_bun(self, burger, mock_ingredient_factory):
        ingredient = mock_ingredient_factory(name="Ketchup", price=50, ing_type=INGREDIENT_TYPE_SAUCE)
        burger.add_ingredient(ingredient)
        with pytest.raises(AttributeError):
            burger.get_receipt()

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


def test_burger_wit_bun_and_ingredient():
    bun_name = 'unbelievable_bun'
    bun = Bun(name=bun_name, price=700)
    ingredient = Ingredient('INGREDIENT_TYPE_SAUCE', 'invisible_sauce', 0.0)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert ingredient.get_name() in receipt and ingredient.get_type().lower() in receipt


def test_burger_with_bun():
    bun = Bun(name='huge_bun', price=500)
    burger = Burger()
    burger.set_buns(bun)
    receipt = burger.get_receipt()
    assert bun.get_name() in receipt


def test_burger_wit_filling():
    bun_name = 'unbelievable_bun'
    bun = Bun(name=bun_name, price=550)
    ingredient = Ingredient('INGREDIENT_TYPE_FILLING', 'unicorn meat', 100)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert burger.get_price() == 1200 and ingredient.get_name() in receipt

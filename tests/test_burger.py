import random

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


def test_burger_wit_bun_and_some_ingredient():  # в чек вошло название ингредиента, т.е. ингредиент был успешно добавлен
    bun_name = 'unbelievable_bun'
    bun = Bun(name=bun_name, price=700)
    ingredient = Ingredient('INGREDIENT_TYPE_SAUCE', 'some_sauce', 0.0)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert ingredient.get_name() in receipt


def test_burger_with_bun():  # в чек вошло название булочки, т.е. булочка была успешно добавлена
    bun = Bun(name='huge_bun', price=500)
    burger = Burger()
    burger.set_buns(bun)
    receipt = burger.get_receipt()
    assert bun.get_name() in receipt


def test_burger_wit_filling_price():  # цена булочки и ингредиента суммарно ровна 1200, метод get_price считает верно
    bun_name = 'unbelievable_bun'
    bun = Bun(name=bun_name, price=550)
    ingredient = Ingredient('INGREDIENT_TYPE_FILLING', 'unicorn meat', 100)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    assert burger.get_price() == 1200


def test_set_buns(burger, new_greate_bun):  # добавляемая булочка добавилась в бургер
    burger.set_buns(new_greate_bun)
    assert burger.bun == new_greate_bun


def add_ingredient(burger, new_greate_ingredient):
    burger.add_ingredient(new_greate_ingredient)
    assert burger.ingredients == new_greate_ingredient


def test_get_price(burger, new_greate_bun, new_greate_ingredient):
    # Установить булочку
    burger.set_buns(new_greate_bun)

    # Добавить ингредиенты
    burger.add_ingredient(new_greate_ingredient)

    # Рассчитать ожидаемую цену
    expected_price = new_greate_bun.get_price() * 2 + new_greate_ingredient.get_price()

    # Проверить, что метод get_price возвращает правильную цену
    assert burger.get_price() == expected_price


def test_get_receipt(burger, new_greate_bun, ingredients):
    burger.set_buns(new_greate_bun)
    burger.add_ingredient(ingredients[0])
    burger.add_ingredient(ingredients[1])
    burger.add_ingredient(ingredients[2])
    receipt = burger.get_receipt()

    added_ingredient_names = [ingredient.get_name() for ingredient in ingredients[:3]]
    assert added_ingredient_names[random.randint(0, 2)] in receipt


def test_move_ingredient(burger):
    burger.set_buns(Bun("black bun", 100))  # Установим булку
    ingredient1 = Ingredient('INGREDIENT_TYPE_SAUCE', "hot sauce", 100)
    ingredient2 = Ingredient('INGREDIENT_TYPE_SAUCE', "sour cream", 200)
    burger.add_ingredient(ingredient1)  # Добавим первый ингредиент
    burger.add_ingredient(ingredient2)  # Добавим второй ингредиент

    burger.move_ingredient(1, 0)  # Переместим ингредиент с позиции 1 на позицию 0

    # Проверим, что ингредиенты на новых позициях соответствуют ожидаемым
    assert burger.ingredients[0].get_name() == "sour cream"


def test_remove_ingredient(burger):
    burger.set_buns(Bun("black bun", 100))  # Установим булку
    ingredient1 = Ingredient('INGREDIENT_TYPE_SAUCE', "hot sauce", 100)
    ingredient2 = Ingredient('INGREDIENT_TYPE_SAUCE', "sour cream", 200)
    burger.add_ingredient(ingredient1)  # Добавим первый ингредиент
    burger.add_ingredient(ingredient2)  # Добавим второй ингредиент

    burger.remove_ingredient(1)  # Удалим ингредиент с позиции 1

    # Проверим, что второй ингредиент удалён
    assert len(burger.ingredients) == 1

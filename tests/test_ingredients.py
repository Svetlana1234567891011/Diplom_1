import random
import pytest

from praktikum.ingredient import Ingredient


def test_ingredients(mock_ingredient, mock_db):  # метод get_name возвращает имя ингредиента из объекта в списке,
    # и из отдельного объекта

    list_of_all_ingredients = mock_db.available_ingredients()
    list_of_all_ingredient_names = [ingredient.get_name() for ingredient in list_of_all_ingredients]

    assert mock_ingredient.get_name() in list_of_all_ingredient_names


def test_get_name():
    ingredient = Ingredient('INGREDIENT_TYPE_SAUCE', "ketchup", 30)
    assert ingredient.get_name() == "ketchup"


def test_get_name_added_early(new_greate_ingredient):
    ingredient = new_greate_ingredient
    assert ingredient.get_name() == "lettuce"


def test_get_ingredient_price_added_early(new_greate_ingredient):
    ingredient = new_greate_ingredient
    assert ingredient.get_price() == 50


def test_get_price_ingredient(mock_ingredient):
    assert mock_ingredient.get_price() == 100


def test_get_name_ingredient(mock_ingredient):
    assert mock_ingredient.get_name() == "hot sauce"


def test_get_type(mock_ingredient):
    assert mock_ingredient.get_type() == 'INGREDIENT_TYPE_SAUCE'


def test_get_name_ingredient_by_method(mock_ingredient):
    assert mock_ingredient.get_name() == mock_ingredient.name


def test_ingredients_random(mock_db):
    list_of_all_ingredients = mock_db.available_ingredients()
    length = len(list_of_all_ingredients) - 1
    random_number_new = random.randint(0, length)
    random_ingredient = list_of_all_ingredients[random_number_new]
    name_with_method = random_ingredient.get_name()
    name_from_base = random_ingredient.name
    assert name_from_base == name_with_method


def test_ingredients_any(mock_db):
    list_of_all_ingredients = mock_db.available_ingredients()
    length = len(list_of_all_ingredients) - 1
    random_number_new = random.randint(0, length)
    random_ingredient = list_of_all_ingredients[random_number_new]
    name_with_method = random_ingredient.get_name()
    name_from_base = random_ingredient.name
    assert name_from_base == name_with_method

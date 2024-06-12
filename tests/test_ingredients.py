import random
import pytest
from praktikum.database import Database


def test_ingredients(mock_ingredient):
    db = Database()
    list_of_all_ingredients = db.available_ingredients()
    list_of_all_ingredient_names = [ingredient.get_name() for ingredient in list_of_all_ingredients]

    assert mock_ingredient.get_name() in list_of_all_ingredient_names


def test_ingredients_random():
    db = Database()
    list_of_all_ingredients = db.available_ingredients()
    length = len(list_of_all_ingredients) - 1
    random_number_new = random.randint(0, length)
    random_ingredient = list_of_all_ingredients[random_number_new]
    name_with_method = random_ingredient.get_name()
    name_from_base = random_ingredient.name
    assert name_from_base == name_with_method


def test_ingredients_any():
    db = Database()
    list_of_all_ingredients = db.available_ingredients()
    length = len(list_of_all_ingredients) - 1
    random_number_new = random.randint(0, length)
    random_ingredient = list_of_all_ingredients[random_number_new]
    name_with_method = random_ingredient.get_name()
    name_from_base = random_ingredient.name
    assert name_from_base == name_with_method


import pytest
from praktikum.database import Database


def test_get_buns_from_database():
    db = Database()
    buns = db.available_buns()
    assert len(buns) > 0


def test_get_ingredients_from_database():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) > 0


@pytest.mark.parametrize('expected_list', [["black bun", "white bun", "red bun"]])
def test_get_list_buns_names(expected_list):
    db = Database()
    available_buns = db.available_buns()
    actual_list = [bun.name for bun in available_buns]  # Получаем список имен булочек из списка объектов
    assert expected_list == actual_list


def test_ingredients_list_price(mock_db):
    db = Database()
    mock_ingredients = mock_db.available_ingredients()
    real_ingredients = db.available_ingredients()

    # Получаем списки цен для обоих списков
    mock_ingredient_price = [ingredient.get_price() for ingredient in mock_ingredients]
    real_ingredient_price = [ingredient.get_price() for ingredient in real_ingredients]

    assert mock_ingredient_price == real_ingredient_price

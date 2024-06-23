from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING



import pytest
from praktikum.ingredient import Ingredient
from unittest.mock import Mock

@pytest.fixture
def burger():
    return Burger()
@pytest.fixture
def new_greate_ingredient():
    # Создаем новый ингредиент
    new_ingredient = Ingredient('INGREDIENT_TYPE_FILLING', "lettuce", 50)

    return new_ingredient


# Фикстура для мок-объекта ингредиента
@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 100
    ingredient.get_type.return_value = "INGREDIENT_TYPE_SAUCE"
    ingredient.name = "hot sauce"
    return ingredient


@pytest.fixture
def new_greate_bun():
    # Создаем новую булочку
    new_bun = Bun('magic bun', 100)

    return new_bun


# Фикстура для мок-объекта ингредиента
@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "magic bun"
    bun.get_price.return_value = 100
    bun.name = "magic bun"
    return bun


@pytest.fixture
def mock_db():
    db = Mock(spec=Database)
    db.available_ingredients.return_value = [
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
    ]
    return db

@pytest.fixture
def ingredients():
    return [
        Ingredient('SAUCE', "hot sauce", 100),
        Ingredient('SAUCE', "sour cream", 200),
        Ingredient('SAUCE', "chili sauce", 300),
        Ingredient('FILLING', "cutlet", 100),
        Ingredient('FILLING', "dinosaur", 200),
        Ingredient('FILLING', "sausage", 300)
    ]


@pytest.fixture
def buns():
    return [
        Bun('hot bun', 100),
        Bun('fake bun', 200),
        Bun('simple bun',  300)

    ]

@pytest.fixture
def mock_db_buns():
    db = Mock(spec=Database)
    db.available_buns.return_value = [
        Bun('black bun', 100),
        Bun('white bun', 200),
        Bun('red bun', 300)
    ]
    return db

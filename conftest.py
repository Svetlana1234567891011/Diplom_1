import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


# Фикстура для мок-объекта ингредиента
@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 100
    ingredient.get_type.return_value = "INGREDIENT_TYPE_SAUCE"
    return ingredient


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

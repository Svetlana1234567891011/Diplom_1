import random
import pytest
from praktikum.database import Database


@pytest.mark.parametrize('expected_name', ["black bun", "white bun", "red bun"])
def test_get_bun_name_returns_value(expected_name):
    db = Database()
    list_of_buns = db.available_buns()

    # Проверяем, есть ли булочка с ожидаемым именем в списке
    names = [bun.get_name() for bun in list_of_buns]
    assert expected_name in names


@pytest.mark.parametrize('expected_name, price', [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def test_get_bun_name_by_price_new(expected_name, price):
    db = Database()
    list_of_buns = db.available_buns()

    # Найти булочку по цене с использованием filter
    bun = next(filter(lambda b: b.get_price() == price, list_of_buns))

    assert bun.get_name() == expected_name, f"Expected bun name '{expected_name}' but got '{bun.get_name()}'"


def test_get_bun_name_by_anyway():
    db = Database()
    list_of_buns = db.available_buns()
    bun = list(list_of_buns)[0]  # выбрать первый объект из списка
    bun_with_method = bun.get_name()
    bun_from_object = bun.name
    assert bun_with_method == bun_from_object


@pytest.mark.parametrize('expected_price', [100, 200, 300])
def test_get_bun_price_returns_value(expected_price):
    db = Database()
    list_of_buns = db.available_buns()

    # Проверяем, есть ли булочка с ожидаемым именем в списке
    price = [bun.get_price() for bun in list_of_buns]
    assert expected_price in price


@pytest.mark.parametrize('name, expected_price', [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def test_get_bun_name_by_price_new(expected_price, name):
    db = Database()
    list_of_buns = db.available_buns()

    # Найти булочку по имени с использованием filter
    bun = next(filter(lambda b: b.get_name() == name, list_of_buns))

    assert bun.get_price() == expected_price, f"Expected bun name '{expected_price}' but got '{bun.get_price()}'"


def test_get_bun_name_by_price_first():
    db = Database()
    list_of_buns = db.available_buns()
    bun = list(list_of_buns)[0]  # выбрать первый объект из списка
    bun_with_method = bun.get_price()
    bun_from_object = bun.price
    assert bun_with_method == bun_from_object


def test_get_bun_name_by_price_len():
    db = Database()
    list_of_buns = db.available_buns()
    length = len(list_of_buns)-1
    random_number = random.randint(0, length)
    bun = list_of_buns[random_number]
    bun_with_method = bun.get_price()
    bun_from_object = bun.price
    assert bun_with_method == bun_from_object






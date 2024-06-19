import random
import pytest

from praktikum.bun import Bun


def test_get_name():
    bun = Bun('super bun', 30)
    assert bun.get_name() == 'super bun'


def test_get_name_added_early(new_greate_bun):
    bun = new_greate_bun
    assert bun.get_name() == "magic bun"


def test_get_ingredient_price_added_early(new_greate_bun):
    bun = new_greate_bun
    assert bun.get_price() == 100


def test_bun_price_added_early_check_mehtod_get(new_greate_bun):
    bun = new_greate_bun
    assert bun.get_price() == bun.price


def test_get_price_bun(mock_bun):
    assert mock_bun.get_price() == 100


def test_get_name_bun(mock_bun):
    assert mock_bun.get_name() == "magic bun"


def test_get_name_bun_by_method(mock_bun):
    assert mock_bun.get_name() == mock_bun.name


@pytest.mark.parametrize('expected_name', ["black bun", "white bun", "red bun"])
def test_get_bun_name_returns_value(expected_name, mock_db_buns):
    list_of_buns = mock_db_buns.available_buns()  # получаем список булочек из мока, имитирующего получение из базы

    # Проверяем, есть ли булочка с ожидаемым именем в списке
    names = [bun.get_name() for bun in list_of_buns]
    assert expected_name in names


@pytest.mark.parametrize('expected_name, price', [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def test_get_bun_name_by_price_new(expected_name, price, buns):
    list_of_buns = buns

    # Найти булочку по цене с использованием filter
    bun = next(filter(lambda b: b.get_price() == price, list_of_buns))

    assert bun.get_name() == expected_name, f"Expected bun name '{expected_name}' but got '{bun.get_name()}'"


def test_get_bun_name_by_anyway(buns):
    list_of_buns = buns  # получаем все булочки
    bun = list(list_of_buns)[0]  # выбрать первый объект из списка
    bun_with_method = bun.get_name()  # получаем методом get имя первой в списке булочки
    bun_from_object = bun.name  # получаем имя через атрибут объекта
    assert bun_with_method == bun_from_object  # имена совпадают -> метод get_name работает корректно


@pytest.mark.parametrize('expected_price', [100, 200, 300])
def test_get_bun_price_returns_value(expected_price, buns):  # получаем все булочки

    list_of_buns = buns

    # Проверяем, есть ли булочка с ожидаемой ценой в списке
    price = [bun.get_price() for bun in list_of_buns]
    assert expected_price in price


@pytest.mark.parametrize('name, expected_price', [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def test_get_bun_name_by_price_new(expected_price, name, mock_db_buns):
    list_of_buns = mock_db_buns.available_buns()

    # Найти булочку по имени с использованием filter
    bun = next(filter(lambda b: b.get_name() == name, list_of_buns))

    assert bun.get_price() == expected_price, f"Expected bun name '{expected_price}' but got '{bun.get_price()}'"


def test_get_bun_name_by_price_first(mock_db_buns):
    list_of_buns = mock_db_buns.available_buns()
    bun = list(list_of_buns)[0]  # выбрать первый объект из списка
    bun_with_method = bun.get_price()
    bun_from_object = bun.price
    assert bun_with_method == bun_from_object


def test_get_bun_name_by_price_len(mock_db_buns):
    list_of_buns = mock_db_buns.available_buns()
    length = len(list_of_buns) - 1
    random_number = random.randint(0, length)
    bun = list_of_buns[random_number]
    bun_with_method = bun.get_price()
    bun_from_object = bun.price
    assert bun_with_method == bun_from_object

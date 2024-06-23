import pytest

from praktikum.bun import Bun


def test_get_name():
    bun = Bun('super bun', 30)
    assert bun.get_name() == 'super bun'


def test_get_price_bun(mock_bun):
    assert mock_bun.get_price() == 100

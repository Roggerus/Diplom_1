import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 50
    return bun

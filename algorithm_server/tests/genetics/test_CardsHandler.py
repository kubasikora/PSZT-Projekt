import pytest
from genetics import CardsHandler

def test_name_exists():
    assert CardsHandler

def test_evaluate_first_arg():
    handler = CardsHandler(4, 6)
    result = handler.evaluate()
    assert result['A'] == 4

def test_evaluate_second_arg():
    handler = CardsHandler(4, 6)
    result = handler.evaluate()
    assert result['B'] == 6

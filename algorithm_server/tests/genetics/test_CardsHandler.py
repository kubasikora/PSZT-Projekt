import pytest
from genetics import CardsHandler

def test_name_exists():
    assert CardsHandler

def test_if_result_A_is_an_array():
    handler = CardsHandler(45,53)
    result = handler.evaluate()
    assert isinstance(result['A'], list)

def test_if_result_B_is_an_array():
    handler = CardsHandler(45,53)
    result = handler.evaluate()
    assert isinstance(result['B'], list)

def test_if_throws_typeerror_on_string_arg_A():
    with pytest.raises(TypeError):
        handler = CardsHandler('45', 34)

def test_if_throws_typeerror_on_string_arg_B():
    with pytest.raises(TypeError):
        handler = CardsHandler(45, '34')

def test_if_throws_typeerror_on_list_arg_A():
    with pytest.raises(TypeError):
        handler = CardsHandler([45], 34)

def test_if_throws_typeerror_on_list_arg_A():
    with pytest.raises(TypeError):
        handler = CardsHandler(45, [34])

def test_if_throws_error_on_insufficient_arguments():
    with pytest.raises(TypeError):
        handler = CardsHandler(34)
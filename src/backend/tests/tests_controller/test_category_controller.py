import sys
sys.path.append('.')
import pytest

from src.backend.controller.base_controller import BaseController
from src.backend.controller.category_controller import CategoryController


@pytest.fixture
def create_instance():
    return CategoryController()


def test_sport_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, CategoryController)


def test_read_all_should_return_list(create_instance):
    result = create_instance.read_all()
    assert isinstance(result, list)


def test_read_by_id_with_invalid_id_should_raise_exception(create_instance):
    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(42342)
    assert str(exc.value) == 'Item not found in the database for this id.'

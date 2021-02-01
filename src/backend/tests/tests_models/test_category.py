import sys
sys.path.append('.')

from src.backend.model.category import Category
import pytest

@pytest.mark.parametrize("name, description", [
    ("N", ''),
    ('N' * 100, 'D' * 200),
    ('N' * 75, 'D' * 150)
])
def test_category_instance(name, description):
    cat = Category(name, description)
    assert isinstance(cat, Category)

def test_name_min_len():
    name = "N"
    description = ''
    cat = Category(name, description)
    assert cat.name is name

def test_name_not_none():
    with pytest.raises(TypeError):
        cat = Category(None, 'some description')

@pytest.mark.parametrize("name, description", [
    (10, 'some description'),
    (10.5, 'some description'),
    (True, 'some description')
])

def test_name_not_str(name, description):
    with pytest.raises(TypeError):
        cat = Category(name, description)

def test_name_not_empty():
    with pytest.raises(ValueError):
        cat = Category('' * 10, 'some description')

def test_name_max_len():
    with pytest.raises(ValueError):
        cat = Category('N' * 101, 'some description')

def test_description_not_none():
    with pytest.raises(TypeError):
        cat = Category('Some name', None)

def test_description_not_str():
    with pytest.raises(TypeError):
        cat = Category('Some name', 10)

def test_description_max_len():
    with pytest.raises(ValueError):
        cat = Category("Some name", 'D' * 201)
import sys
sys.path.append('.')

import pytest
from src.backend.model.category import Category
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.backend.dao.category_dao import CategoryDao


@pytest.fixture
def create_category():
    return Category("Teste-03fev2021", "testado")


@pytest.fixture
def create_instance():
    dao = CategoryDao()
    return dao


def test_instance(create_instance):
    assert isinstance(create_instance, CategoryDao)


def test_save(create_category,create_instance):
    cat = create_instance.save(create_category)

    assert cat.id_ is not None
    create_instance.delete(cat)


def test_not_save(create_instance):
    with pytest.raises(UnmappedInstanceError):
        create_instance.save('test')


def test_read_by_id(create_category,create_instance):
    cat = create_instance.save(create_category)
    cat_read = create_instance.read_by_id(cat.id_)

    assert isinstance(cat_read, Category)
    create_instance.delete(cat_read)


def test_not_read_by_id(create_instance):
    with pytest.raises(TypeError):
        create_instance.read_by_id('id_')


def test_read_all(create_instance):
    cat_read = create_instance.read_all()
    assert isinstance(cat_read, list)


def test_delete(create_category,create_instance):
    cat = create_instance.save(create_category)
    cat_read = create_instance.read_by_id(cat.id_)
    create_instance.delete(cat_read)
    cat_read = create_instance.read_by_id(cat.id_)

    assert cat_read is None


def test_not_delete(create_instance):
    with pytest.raises(UnmappedInstanceError):
        create_instance.delete('cat')

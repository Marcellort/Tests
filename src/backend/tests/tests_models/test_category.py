import sys
sys.path.append('.')

from src.backend.model.category import Cateogry


name = 'valid name'
description = 'valid description'


class Test_category_model:

    def test_category_instance(self):
        name = 'valid name'
        description = 'valid description'
        category_model = Cateogry(name, description)
        assert isinstance(category_model, Cateogry)

    def test_name_no_string(self):
        try:
            category_model = Cateogry(1, description)
        except Exception as e:
            assert isinstance(e, TypeError)

    def test_name_empty(self):
        try:
            category_model = Cateogry('', description)
        except Exception as e:
            assert isinstance(e, ValueError)

    def test_name_large_len(self):
        try:
            category_model = Cateogry('a' * 101, description)
        except Exception as e:
            assert isinstance(e, ValueError)

    def test_description_no_string(self):
        try:
            category_model = Cateogry(name, 1)
        except Exception as e:
            assert isinstance(e, TypeError)

    def test_description_empty(self):
        try:
            category_model = Cateogry(name, '')
        except Exception as e:
            assert isinstance(e, ValueError)

    def test_description_empty(self):
        try:
            category_model = Cateogry(name, 'a'*101)
        except Exception as e:
            assert isinstance(e, ValueError)

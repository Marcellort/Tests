import sys
sys.path.append('.')
from src.backend.dao.base_dao import BaseDao
from src.backend.model.category import Category


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)

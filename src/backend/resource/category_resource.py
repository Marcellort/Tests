from flask_restful import marshal_with, fields

from src.backend.dao.category_dao import CategoryDao
from src.backend.model.category import Category
from src.backend.resource.base_resource import BaseResource


class CategoryResource(BaseResource):
    fields = {
        "id_":  fields.Integer,
        "name":  fields.String,
        "description":  fields.String
    }

    def __init__(self):
        self.__dao = CategoryDao()
        self.__model = Category
        super().__init__(self.__dao, self.__model)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)

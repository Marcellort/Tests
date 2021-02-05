from flask import request
from flask_restful import Resource
from src.backend.dao.base_dao import BaseDao


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, type_model: type):
        self.__dao = dao
        self.__type_model = type_model

    def get(self, id=None):
        if id:
            return self.__dao.read_by_id(id)
        return self.__dao.read_all()

    def post(self):
        data = request.json
        item = self.__type_model(**data)
        return self.__dao.save(item)

    def put(self, id):
        data = request.json
        if data['id_'] == id:
            item = self.__dao.read_by_id(id)
            for key, value in data.items():
                setattr(item, key, value)
            return self.__dao.save(item)
        return None, 404

    def delete(self, id):
        data = request.json
        if data['id_'] == id:
            item = self.__dao.read_by_id(id)
            self.__dao.delete(item)
            return None, 204
        return None, 404

import sys
sys.path.append('.')
from src.backend.model.base_model import BaseModel
from src.backend.dao.session import Session


class BaseDao:
    def __init__(self, type_model):
        self.__type = type_model

    def save(self, model: BaseModel) -> BaseModel:
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type).order_by('name').all()
            return result

    def read_by_id(self, id_) -> BaseModel:
        if isinstance(id_, int):
            with Session() as session:
                result = session.query(self.__type).filter_by(id_=id_).first()
            return result
        else:
            raise TypeError('id must be integer.')

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()

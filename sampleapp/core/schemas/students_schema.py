from ..config import ma
from ..models.students_model import Students


class StudentsSchema(ma.SQLAlchemyAutoSchema):
    __envelope__ = {'single': None, 'many': 'students'}
    class Meta:
        model = Students
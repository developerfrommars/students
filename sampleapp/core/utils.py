from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from .models.students_model import Students
from .schemas.students_schema import StudentsSchema

def check_if_user_exists(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            student = Students.query.filter(Students.id == kwargs.get('id')).first()
        except (SQLAlchemy.exc.SQLAlchemyError, SQLAlchemy.exc.DBAPIERROR):
            return {"err", "err"}, 500
        if not student:
            return {"err": "err"}, 404
        rv = func(args, **kwargs)
        return rv
    return wrapper
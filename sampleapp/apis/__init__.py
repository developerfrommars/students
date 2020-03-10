from flask_restplus import Api

from .students_namespace import api as students_api

api = Api(
    title = 'Students api',
    version = '1.0'
)

api.add_namespace(students_api)
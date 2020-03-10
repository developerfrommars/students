import os

from flask import Flask, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restplus import Api, Resource, Namespace, fields
from core.models.students_model import Students
from core.schemas.students_schema import StudentsSchema
from core.utils import check_if_user_exists
from core.config import db, ma

api = Namespace('students', description='Students related ops')

payload_model = api.model('data', {
    'firstname': fields.String,
    'lastname': fields.String,
    'spec': fields.String
})


@api.route('/students')
class index(Resource):
    def get(self):
        students_schema = StudentsSchema(many=True)
        spec_requested = request.args.get('specialization')
        if spec_requested:
            return students_schema.dump(Students.query.filter(Students.spec == spec_requested).all())
        return students_schema.dump(Students.query.all())
    
    @api.expect(payload_model)
    def post(self):
        _student = Students()

        # Sketchy way of parsing requests, for sure there is a better way. 
        # It iterates through JSON objects and assigns object's values with them.
        for key in api.payload.keys():
            setattr(_student, key, api.payload.get(key))
        try:
            db.create_all()
            db.session.add(_student)
            db.session.commit()
        except (SQLAlchemy.exc.SQLAlchemyError, SQLAlchemy.exc.DBAPIERROR):
            return {"error": "error"}, 500
        return {"url": f"{url_for('index')}/{_student.id}"}, 201

@api.route('/students/<int:id>')
class student_id(Resource):
    @check_if_user_exists
    def get(self, id):
        students_schema = StudentsSchema(many=False)
        try:
            student = Students.query.filter(Students.id == id).first()
        except (SQLAlchemy.exc.SQLAlchemyError, SQLAlchemy.exc.DBAPIERROR):
            return {"error": "error"}, 500
        rv =  students_schema.dump(student) 
        return rv
    
    @api.expect(payload_model)
    @check_if_user_exists
    def put(self, id):
        students_schema = StudentsSchema(many=False)
        student = Students.query.filter(Students.id == id).first()
        for key in api.payload.keys():
            setattr(student, key, api.payload.get(key))
        try:
            db.session.commit()
        except (SQLAlchemy.exc.SQLAlchemyError, SQLAlchemy.exc.DBAPIERROR):
            return {"error": "error"}, 500
        return students_schema.dump(student)

    def delete(self, id):
        Students.query.filter(Students.id == id).delete()
        try:
            db.session.commit()
        except (SQLAlchemy.exc.SQLAlchemyError, SQLAlchemy.exc.DBAPIERROR):
            return {"error", "error"}
        return {"success": "user deleted"}, 200


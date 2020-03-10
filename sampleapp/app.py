import os

from flask import Flask
from core.config import db, ma
from apis import api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"] 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
db.init_app(app)
ma.init_app(app)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
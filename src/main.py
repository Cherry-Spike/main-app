from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class BookUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'book_id', name='user_book_unique')


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

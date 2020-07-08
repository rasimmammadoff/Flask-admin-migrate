from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.secret_key='secret_key'

db.init_app(app)
migrate.init_app(app,db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    price = db.Column(db.Float,nullable=False)
    name = db.Column(db.String(20),nullable=False)
    date = db.Column(db.DateTime(),default=datetime.utcnow)

admin = Admin(app)
admin.add_view(ModelView(Product,db.session))

@app.route('/')
def home():
    return "Usage of Flask migrate and admin"


if __name__ == '__main__':
    manager.run()
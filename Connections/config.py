from flask import Flask

DB_USER = 'mzwakhe'
DB_PASSWORD = 'R3qu3st3r2021$'
DB_NAME = 'todo'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'

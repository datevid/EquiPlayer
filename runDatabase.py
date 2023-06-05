from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from AppRoot.model.database import create_database,check_tables_exist
from AppRoot.model.models import User,db
from AppRoot.model.models import Player

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# initialize the app with the extension
db.init_app(app)
#db=SQLAlchemy(app)

def poblate():
    print("Se poblará la tabla User")
    # Crea algunos usuarios
    user1 = User(name='John', email='john@example.com')
    user2 = User(name='Alice', email='alice@example.com')

    # Crea algunos jugadores
    player1 = Player(fullname='Lionel Messi', sizeplayer=170)
    player2 = Player(fullname='Cristiano Ronaldo', sizeplayer=187)

    # Agrega los objetos a la sesión y los guarda en la base de datos
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(player1)
    db.session.add(player2)
    db.session.commit()
    return 'User created successfully!'
    
with app.app_context():
    if(check_tables_exist(db)):
        print("tablas existentes")
    else:
        print("no existen las tablas y la DB, se crearán")
        create_database(db)
        poblate()
    
    
    
  
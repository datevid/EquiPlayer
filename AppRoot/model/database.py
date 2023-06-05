# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from .models import db

def create_database(db):
    db.create_all()
    print("Base de datos creada exitosamente")

    # Obtén información sobre las tablas existentes
    inspector = db.inspect(db.engine)
    table_names = inspector.get_table_names()
    print("Tablas existentes:")
    for table_name in table_names:
        print(table_name)

def check_tables_exist(db):
    inspector = db.inspect(db.engine)
    table_names = inspector.get_table_names()

    return 'user' in table_names and 'player' in table_names
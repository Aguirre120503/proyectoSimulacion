# create_db.py
from app.database import Base, engine
from app import models

print("Creando las tablas en SQLite...")
Base.metadata.create_all(bind=engine)
print("¡Listo!")

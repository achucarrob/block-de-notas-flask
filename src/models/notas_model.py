# Aqui creamos el modelo de la tabla para la db
from flask_sqlalchemy import SQLAlchemy
# instancia de la clase SQLalchemy 
db = SQLAlchemy()

class Notas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    nota = db.Column(db.Integer, nullable=False)

    def __init__(self, titulo, nota):
        self.titulo = titulo
        self.nota = nota

# Esta tabla se crea cuando ejecutamos el archivo app.py
# Configuraciones del programa
# dependencias
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# modulos
from models.notas_model import Notas, db
from routes.notas_routes import notas

app = Flask(__name__)
# Registro de blueprint
app.register_blueprint(notas)

# conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Esta configuracion por defecto es True
db.init_app(app)

# Crear las tablas
with app.app_context():
    db.create_all()
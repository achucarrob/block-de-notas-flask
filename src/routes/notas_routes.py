# Dependencias 
from flask import Blueprint, render_template, request, url_for, redirect

# Modulos 
from models.notas_model import Notas, db
# Crear blueprint 
notas = Blueprint("notas", __name__)

# Read 
@notas.route('/')
def index():
    notas_guardadas = Notas.query.all()
    return render_template('index.html', notas_guardadas = notas_guardadas)

# Create
@notas.route('/crear', methods=['GET', 'POST'])
def crear_nota():
    if request.method == 'POST':
        titulo = request.form['titulo']
        nota = request.form['nota']

        nueva_nota = Notas(titulo,nota)

        db.session.add(nueva_nota)
        db.session.commit()

        return render_template('index.html')
    return render_template('index.html')

# Update 
@notas.route('/actualizar/<id>', methods=['GET', 'POST'])
def actualizar(id):
    nota_seleccionada = Notas.query.get(id)

    if request.method == 'POST':
        nota_seleccionada.titulo = request.form['titulo']
        nota_seleccionada.nota = request.form['nota']
        
        db.session.commit()
        return redirect(url_for('notas.index'))
    return render_template('actualizar.html' , nota_seleccionada= nota_seleccionada)

# Delete 
@notas.route('/eliminar/<id>')
def eliminar(id):
    nota_seleccionada = Notas.query.get(id)
    db.session.delete(nota_seleccionada)
    db.session.commit()

    return redirect(url_for('notas.index'))
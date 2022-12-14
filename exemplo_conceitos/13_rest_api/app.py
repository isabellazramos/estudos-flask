from flask import Flask, render_template, request, url_for, redirect, Response
from models import db, Estudante
import json

app = Flask(__name__, template_folder='templates')
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'


@app.route('/')
def index():
    # estudantes = Estudante.query.all()
    # result = [e.to_dict() for e in estudantes]
    rows = db.session.execute("select * from estudante").fetchall()
    result = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute("select * from estudante where id = %s" %id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")


@app.route('/add', methods=['POST'])
def add():
    estudante = Estudante(nome= request.form['nome'],idade= request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")


@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")


@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")


if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)

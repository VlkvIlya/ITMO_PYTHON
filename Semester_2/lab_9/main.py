from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('Заметки')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note_name = db.Column(db.String(300))
    important = db.Column(db.Boolean, default=False)


@app.route('/')
def main():
    notes = Note.query.all()
    return render_template('index.html', notes_list=notes)


@app.route('/important/<note_id>', methods=['PATCH'])
def modify_important(note_id):
    note = Note.query.get(note_id)
    note.important = request.json['important']
    db.session.commit()


@app.route('/add', methods=['POST'])
def add_note():
    data = request.json
    note = Note(**data)
    db.session.add(note)
    db.session.commit()


@app.route('/clear', methods=['DELETE'])
def clear_notes():
    Note.query.delete()
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
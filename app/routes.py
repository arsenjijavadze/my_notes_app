from flask import Blueprint, request, flash, redirect, url_for, render_template
from app import db
from app.models import Note
from app.forms import NoteForm

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')


@main_routes.route('/notes')
def notes():
    try:
        notes = Note.query.all()
        return render_template('notes.html', notes=notes)
    except Exception as e:
        print(f"Error accessing database: {e}")
        flash('Error accessing the database', 'error')
        return render_template('notes.html', notes=[])

@main_routes.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    form = NoteForm()
    if request.method == 'POST':
        print("FormData:", request.form)
    if form.validate_on_submit():
        note = Note(title=form.title.data, content=form.content.data)
        db.session.add(note)
        db.session.commit()
        flash('Your note has been created!', 'success')
        return redirect(url_for('main.notes'))
    return render_template('create_note.html', title='New Note', form=form)

@main_routes.route('/notes/<int:note_id>/update', methods=['GET', 'POST'])
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    form = NoteForm()
    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        db.session.commit()
        flash('Your note has been updated!', 'success')
        return redirect(url_for('main.notes'))
    elif request.method == 'GET':
        form.title.data = note.title
        form.content.data = note.content
    return render_template('create_note.html', title='Update Note', form=form)

@main_routes.route('/notes/<int:note_id>/view', methods=['GET'])
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('view_note.html', note=note)

@main_routes.route('/notes/<int:note_id>/edit', methods=['GET', 'POST'])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    form = NoteForm(obj=note)

    if form.validate_on_submit():
        # Update the note's attrubutes from the form data
        note.title = form.title.data 
        note.content = form.content.data
        db.session.commit() # Commit the changes to the database
        return redirect(url_for('main.notes'))
    return render_template('edit_note.html', form=form, note=note)

@main_routes.route('/notes/<int:note_id>/delete', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    flash('Your note has been deleted!', 'success')
    return redirect(url_for('main.notes'))

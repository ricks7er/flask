from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from datetime import datetime
from models import Task

import forms

@app.route('/')
@app.route('/index')
def index():
    tasks=Task.query.all()
    return render_template('index.html',tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t=Task(title=form.title.data,date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Tarea adicionada a la Base de Datos')
        return redirect(url_for('index'))
    return render_template('add.html',form=form)
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

@app.route('/edit/<int:task_id>',methods=['GET','POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Tarea actualizada')
            return redirect(url_for('index'))
        form.title.data=task.title
        return render_template('edit.html',form=form,task_id=task_id)
    return redirect(url_for('index'))
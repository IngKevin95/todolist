from flask import Blueprint, render_template, redirect, request, url_for, g
from todor.auth import login_required
from todor import db
from .models import Task, User


bp = Blueprint('todo',__name__,url_prefix='/todo')

@bp.route('/list')
@login_required
def index():
    tasks = Task.query.all()
    return render_template('todo/index.html', tasks = tasks)

@bp.route('/create', methods= ('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        task = Task(g.user.id, title, desc)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')

def get_task(id):
    task = Task.query.get_or_404(id)
    return task

@bp.route('/update/<int:id>', methods= ('GET', 'POST'))
@login_required
def update(id):
    task = get_task(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['desc']
        task.state = True if request.form.get('state') == 'on' else False
    
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/update.html', task = task)

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    task = get_task(id)

    db.session.delete(task)    
    db.session.commit()
    return redirect(url_for('todo.index'))

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Create app
app = Flask(__name__)
#Config and create databasw
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Creating the model for the tasks
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

#Creating the homepage
@app.route('/')
def index():
    #Queries all tasks and stores them as an iterable variable
    task_list = Task.query.all()
    #renders the html and allows use of the 'task_list' variable
    return render_template('index.html', task_list=task_list)

#Add new task
@app.route('/add', methods=['POST'])
def add():
    #This get the data from the input named 'title'
    title = request.form.get('title')
    ###This BLOCK adds the task
    new_task = Task(title=title, complete=False)
    db.session.add(new_task)
    db.session.commit()
    ###
    #Refresh homepage
    return redirect(url_for('index'))

#Update current tasks
@app.route('/update/<int:task_id>')
def update(task_id):
    #This picks the Task based on its id passed
    task = Task.query.filter_by(id=task_id).first()
    #Sets complete to opposite Ex. True = False
    task.complete = not task.complete
    db.session.commit()
    #Refresh page
    return redirect(url_for('index'))

#Delete current tasks
@app.route('/delete/<int:task_id>')
def delete(task_id):
    #This picks the Task based on its id passed
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

#This runs the app correctly FOR DEV
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
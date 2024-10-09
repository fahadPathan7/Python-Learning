# import libraries

# from flask import Flask (to create a Flask app), render_template (to render HTML templates),
# url_for (to generate URLs), request (to get form data), redirect (to redirect to another URL),
# and SQLAlchemy (to interact with the database)
from flask import Flask, render_template, url_for, request, redirect
# SQLAlchemy is an ORM (Object-Relational Mapping) library for Python. It is used to interact with the database using Python objects.
from flask_sqlalchemy import SQLAlchemy
# datetime module in Python provides classes for manipulating dates and times.
from datetime import datetime


# create a Flask app
# __name__ is a special variable in Python that is used to determine whether the script is being run on its own or being imported as a module.
# If the script is being run on its own, __name__ is set to '__main__'.
# If the script is being imported as a module, __name__ is set to the name of the module.
# In this case, we are running the script on its own, so __name__ is set to '__main__'.
# but if we import this script as a module in another script, __name__ will be set to the name of the module.
# like: from app import app as application and __name__ will be set to 'app'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # the database URI
db = SQLAlchemy(app) # create a database instance


# This Python class defines a Todo model with columns for id, content, completion status, and creation date.
# The __repr__ method is used to represent the object as a string when it is printed. In this case, it returns the task id.
# The Todo class inherits from db.Model, which is a base class for all models in SQLAlchemy.
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) # the task id. The primary_key=True argument specifies that this column is the primary key.
    content = db.Column(db.String(200), nullable=False) # the task content. The nullable=False argument ensures that the content is required.
    completed = db.Column(db.Integer, default=0) # the completion status of the task.
        #The default=0 argument specifies that the task is not completed by default.
    date_created = db.Column(db.DateTime, default=datetime.utcnow) # the creation date of the task.
        #The default=datetime.utcnow argument specifies the current date and time.

    def __repr__(self):
        return '<Task %r>' % self.id # return the task id
            # %r is a conversion specifier that is used to represent the value as a string using repr().
            # `<Task %r>` is a string template that includes the task id. %r is replaced with the task id when the string is formatted.
            # The __repr__ method is called when the object is printed or converted to a string.

# This route initializes the database by creating all the tables defined in the models.
@app.route('/initdb')
def initdb():
    db.create_all() # create all the tables defined in the models
    return 'Database initialized!' # return a message. This message will be displayed in the browser when the route is accessed.

# This route is the home page of the application. It handles both GET and POST requests.
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content'] # get the task content from the form data. `content` is the name of the input field in the form.
        new_task = Todo(content=task_content) # create a new task object with the task content

        # add the new task to the database and commit the changes
        # error handling is used to catch any exceptions that may occur during the database operation.
        try:
            db.session.add(new_task) # add the new task to the session
            db.session.commit() # commit the changes to the database
            return redirect('/') # redirect the user to the home page
        except:
            return 'There was an error'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # get all the tasks from the database and order them by creation date
        return render_template('index.html', tasks=tasks) # render the index.html template with the tasks. tasks is a list of task objects.
            # tasks object is passed so that we can access the tasks from the front-end.

# This route deletes a task from the database based on its id.
@app.route('/delete/<int:id>') # the route URL includes the task id as a parameter. The <int:id> syntax specifies that the id parameter should be an integer.
    # if the id parameter is not an integer, the route will not match and a 404 error will be returned.
def delete(id):
    task_to_delete = Todo.query.get_or_404(id) # get the task with the specified id from the database or return a 404 error if the task does not exist.

    try:
        db.session.delete(task_to_delete) # delete the task from the session
        db.session.commit() # commit the changes to the database
        return redirect('/') # redirect the user to the home page
    except:
        return 'There was an error (delete)'

# This route updates a task in the database based on its id.
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = Todo.query.get_or_404(id) # get the task with the specified id from the database or return a 404 error if the task does not exist.

    if request.method == 'POST':
        task.content = request.form['content'] # update the task content with the new content from the form data.
            # `content` is the name of the input field in the form.
        try:
            db.session.commit() # commit the changes to the database. for update, we only need to commit the changes.
            return redirect('/') # redirect the user to the home page
        except:
            return 'There was an error (update)'
    else:
        return render_template('update.html', task=task, placeholder=task.content) # render the update.html template with the task and the task content.
            # task is the task object that we want to update. placeholder is the current task content.


# This is the main entry point of the application. It runs the Flask app in debug mode.
if __name__== '__main__': # check if the script is being run on its own
    app.run(debug=True) # run the Flask app in debug mode. debug=True enables the debug mode
        # which provides detailed error messages and automatic reloading of the server when changes are made to the code.
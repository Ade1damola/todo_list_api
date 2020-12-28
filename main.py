from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SECRET_KEY'] = 'ashirimi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(12), nullable= False)
    email = db.Column(db.String(28), unique=True, nullable=False)
    public_id = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    todos = db.relationship('Todo', backref='owner', lazy='dynamic')

    def __repr__(self):
        return f'Hi, i am <{self.name}>'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    public_id = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'My task is <{self.task}>'


@app.route('/')
@app.route('/home')
def home():
    return  {
        'message': 'Welcome'
    }, 200

#returns a list of users
@app.route('/users/') #, methods=['GET'])
def all_users():
    return jsonify (
        [
        {
            '_id': user.public_id,
            'name': user.name,
            'email': user.email,
            'is_admin': user.is_admin
        }
        for user in User.query.all()
        ]
        )

#find users by their id number
#@app.route('/users/<id>/')
#def get_user(id):
    #print(id)
    #user = User.query.filter_by(public_id=id).first_or_404()

#find users by their names
@app.route('/users/<name>/')
def get_user(name):
    print(name)
    user = User.query.filter_by(name=name).first_or_404()
    
    return {
            'id': user.public_id,
            'name': user.name,
            'email': user.email,
            'is_admin': user.is_admin
        }

# create a user
@app.route('/user/', methods=['POST'])
def create_user():
    data = request.get_json()
    if not 'name' in data or not 'email' in data:
        return jsonify (
            {
                'error': 'Name and Email not found'
            }
        ), 400
    u = User (
        name= data['name'],
        email= data['email'],
        public_id = str(uuid.uuid4()),
        is_admin= data.get('is admin', False)
    )
    db.session.add(u)
    db.session.commit()
    return {
        'id': u.public_id,
        'name': u.name,
        'email': u.email,
        'is admin': u.is_admin
    }, 201

#update user profile
@app.route('/user/<id>/', methods=['PUT'])
def edit_user(id):
    data = request.get_json()
    if 'name' not in data:
        return jsonify (
            {
                'error': 'Type in the old name'
            }
        ), 400
    user = User.query.filter_by(public_id=id).first_or_404()
    user.name = data['name']
    if 'is admin' in data:
        user.is_admin = data['admin']
    db.session.commit()
    return {
        'id': user.public_id,
        'name': user.name,
        'email': user.email,
        'is_admin': user.is_admin
    }

#delete a user's profile
@app.route('/user/<name>/', methods=['DELETE'])
def delete_user(name):
    user= User.query.filter_by(name=name).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return{
        'message': 'Account deleted'
    }


#returns a list of tasks
@app.route('/todos/')
def get_tasks():
    return jsonify (
        [
            {
                '_id': todo.public_id,
                'your task': todo.task,
                'owner': {
                    'name': todo.owner.name,
                    'email': todo.owner.email,
                    'public_id': todo.owner.public_id
                }
            }
            for todo in Todo.query.all()
        ]
    )

#get a user's task by using their ID
@app.route('/todo/<id>/')
def get_task(id):
    todo = Todo.query.filter_by(public_id=id).first_or_404()
    return jsonify (
        {
            'id': todo.public_id,
            'task name': todo.task,
                'owner':
                {
                    'name': todo.owner.name,
                    'email': todo.owner.email,
                    'user id': todo.owner.public_id
                }
        }
    )

#create a todo task
@app.route('/todo/', methods=['POST'])
def create_task():
    data = request.get_json()
    if not 'task' in data and not 'email' in data:
        return jsonify (
            {
                'error': 'Name and email of creator not stated'
            }
        ), 400
    user = User.query.filter_by(email=data['email']).first() 
    if not user:
        return {
            'error': 'no user with that email'
        }
    is_completed= data.get('is completed', False)
    x = Todo(
        task=data['task'],
        user_id= user.id,
        is_completed= is_completed,
        public_id= str(uuid.uuid4())
    )
    db.session.add(x)
    db.session.commit()
    return {
        'id': x.public_id,
        'task name': x.task,
        'owner':
                {
                    'name': x.owner.name,
                    'email': x.owner.email,
                    'is admin': x.owner.is_admin
                }
    }, 201

#edit a task
@app.route('/todo/<id>/', methods=['PUT'])
def edit_task(id):
    data = request.get_json()
    print(data)
    print('is complete' in data)

    if not 'task' in data or not 'is completed' in data:
        return   {
                'error': 'task name or \'is completed\' not present'
            }, 400

    todo = Todo.query.filter_by(public_id=id).first_or_404()
    todo.task= data.get('task', todo.task)

    if 'is completed' in data:
        todo.is_completed = data['is completed']
    db.session.commit()
    return {
        'id': todo.public_id,
        'task name': todo.task,
        'owner':
                {
                    'name': todo.owner.name,
                    'email': todo.owner.email,
                    'is admin': todo.owner.is_admin
                }
    }, 201

#delete your accont
@app.route('/todo/<id>/', methods=['DELETE'])
def delete_task(id):
    todo = Todo.query.filter_by(public_id=id).first_or_404()
    db.session.delete(todo)
    db.session.commit()

    return{
        'message': 'task deleted'
    }


if __name__ == '__main__':
    app.run(debug=True)
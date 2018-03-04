from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'michi'}
    posts = [
        {
                'author': {'username': 'michael'},
                'body': 'I love chemistry'
         },
        {
                'author': {'username': 'mike'},
                'body': 'I love math'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

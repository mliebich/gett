from flask import render_template
from gettapp import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'michi'}
    posts = [
        {
                'author': {'username': 'michael'}
                'body': 'I love chemistry'
         },
        {
                'author': {'username': 'mike'}
                'body': 'I love math'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
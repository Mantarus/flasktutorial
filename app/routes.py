from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mantarus'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'KOCbKA'},
            'body': 'Meowmeowmeowmeowmeowmeowmeow! :3'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

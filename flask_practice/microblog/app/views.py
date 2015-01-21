from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [ #fake array of posts
        {   #fake post 1
            'author': {'nickname': 'John'},
            'body': 'I love San Francisco, man it\'s so great'

        },
        {   #fake post 2
            'author': {'nickname': 'Eric'},
            'body': 'I like manatees'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = posts)

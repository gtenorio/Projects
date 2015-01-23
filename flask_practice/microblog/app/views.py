from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  #validates user input
        flash('Login requested for OpenId="%s", remember_me=%s' % #displays info quickly
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS']) #else render template

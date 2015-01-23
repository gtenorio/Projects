from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    #user = {'nickname': 'Miguel'}  # test user
    posts = [
        {
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
@oid.loginhandler
def login():
    form = LoginForm()
    if g.user is not None and g.user.is_authenticated(): #checks if user is already logged in
        return redirect(url_for('index'))
    if form.validate_on_submit():  #validates user input
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])        
        '''
        flash('Login requested for OpenId="%s", remember_me=%s' % #displays info quickly
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
        '''
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS']) #else render template
    
@lm.user_loader
def load_user(id):
    return User.query.get(int(id)) #user ids in flask are unicode strings

@app.before_request
def before_request():
    g.user = current_user

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

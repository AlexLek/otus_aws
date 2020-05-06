from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.forms import SignUpForm
import boto3
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler


current_date = datetime.date.today()
#current_log_file = 'signUp_{}.log'.foramt(current_date)


logger = logging.getLogger('Microblog_app')
logger.setLevel(logging.INFO)
#fh = logging.FileHandler('logs/{}'.format(current_log_file))
fh = TimedRotatingFileHandler('logs/signup.log', when='S', interval=30, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# add handler to logger object
logger.addHandler(fh)


s3_client = boto3.client('s3',
    aws_access_key_id='******',
    aws_secret_access_key='*****'
)

BUCKET = "otus-test"



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'UserName'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('SignUp requested for user {}'.format(form.username.data))
        logger.info('New SignUp: {}'.format(form.username.data))
        #s3_client.upload_file('logs/signup.log', BUCKET, 'alekarev/test.log')
        return redirect(url_for('index'))
    return render_template('signup.html',  title='Sign Up', form=form)
    #logger.info('New SignUp: {}'.format(form.username.data))

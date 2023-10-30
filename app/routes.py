from flask import render_template, request, redirect, url_for
from app import app
from app.models import User, Post

@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return redirect(url_for('profile'))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    # TODO: Implement logout functionality
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            error = 'Passwords do not match'
            return render_template('register.html', error=error)
        else:
            user = User(username=username, password=password)
            user.save()
            return redirect(url_for('login'))
    else:
        return render_template('register.html')

@app.route('/profile')
def profile():
    # TODO: Implement user profile functionality
    return render_template('profile.html')
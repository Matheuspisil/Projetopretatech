from flask import render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models.user import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:  # Use hash check in production
            login_user(user)
            return redirect(url_for('profile'))
    return render_template('registration/login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration/register.html', form=form)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

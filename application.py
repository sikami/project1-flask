from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_wtf import Form

app = Flask(__name__)
app.config['SECRET_KEY'] = '53d05301c4425aee8bcf0809850aa2c6'

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html', title = 'home')

@app.route("/register", methods =['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm() 
    return render_template('login.html', title='login', form=form)

@app.route("/content")
def content():
    return "<h1>Welcome to the content of the page</h1>"


if __name__ == '__main__':
    app.run(debug=True) 
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFrom, LoginFrom

app = Flask(__name__)

app.config['SECRET_KEY'] = '8248f73db2ee8da77946a5a0958bb21c'

# This posts is just to show, suppose that we are retrieving that posts data from database.
posts = [
    {
        'title': 'Fire1',
        'author': 'Anshul',
        'content': 'This is fire1.',
        'date_posted': '8-sept-2021'
    },
    {
        'title': 'Fire2',
        'author': 'Rahul',
        'content': 'This is fire2.',
        'date_posted': '7-sept-2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginFrom()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)


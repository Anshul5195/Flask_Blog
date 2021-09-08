from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)


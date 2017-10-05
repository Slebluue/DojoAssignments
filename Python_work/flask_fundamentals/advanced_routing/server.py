from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template("user.html", username=username)

app.run(debug=True)
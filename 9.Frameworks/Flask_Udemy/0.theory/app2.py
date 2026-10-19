from flask import Flask, url_for

# app object instantiation
app = Flask(__name__)

#-----------------------------------------------------------------------------#
# api routes endpoints:
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(dir(url_for))

#-----------------------------------------------------------------------------#
# calling the app
if __name__ == '__main__':
    app.run()

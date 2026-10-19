from flask import Flask, jsonify, request, url_for, redirect, g
import sqlite3

'''
flask:      framework
jsonify:    handling of body data from server
request:    handling requests and url arguments and request body from client
url_for:    get actual URL for a particular route - pass in the function that needs to be called
redirect:   function that handels the redirection of the user to another URL
'''
# app object instantiation and configuration
app = Flask(__name__)
app.config['DEBUG'] = True      # This configuration has to be removed in production
app.config['SECRET_KEY'] = 'this_is_my_secret'

#-----------------------------------------------------------------------------#
# database helping functions:
def connect_db():
    sql = sqlite3.connect('./data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

#-----------------------------------------------------------------------------#
# api routes endpoints:
# using Route Variable '<>'
@app.route('/<name>', methods = ['GET', 'POST'])    # default method is GET, other methods could be defined in methods list
def index(name):
    return f'<h1>You just entered the default route: "{name}"!</h1>'

@app.route('/home/<string:name>')                   # route variable here should be string, other data types (int, float, path and uuid)
@app.route('/home', defaults={'name': 'Lina'})      # defining a default value
def home(name):
    return f'<h1>Home Page!</h1>\n\n<h2>Welcome {name}!!!'

@app.route('/about')
def about():
    return '<h1>About Page!</h1> <p>my name Amr and I love developing new creative things</p>'

# using Request Query String -> request module is needed!
@app.route('/query')
def query():
    name = request.args.get('name')             # gets the value of the name query (case sensitive)
    location = request.args.get('location')     # gets the value of the location query (case sensitive)
    return f'<h1>Hi {name}, from {location}.You are on the query page</h1>'

# Hint: receiving means: client (frontend) requests and server (backend) responds
# sending and receiving data in json format
@app.route('/json', methods = ['GET', 'POST'])
def json():
    if request.method == 'GET':                                     # GET data from server
        return jsonify({'key1' : 'test_value', 'key2': [1,2,3]})    # dict -> json data
    else:                                                           # PUT data into server
        data = request.get_json()                                   # json data -> dict
        print(data)
        reponse = jsonify()
        reponse.status_code = 201
        return reponse

# receiving data in form
@app.route('/theform', methods = ['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return '''  <form method = "POST" action='/theform'>
                        <input type= 'text' name= 'name'>
                        <input type= 'text' name= 'location'>
                        <input type= 'submit' value= 'Submit'>
                    </form>'''
    else:
        name = request.form['name']
        location = request.form['location'] 
        return f'<h1>Hi {name} from {location}, you have submitted the form successfully!</h1>'

#@app.route('/process', methods = ['POST'])
#def process():
#    name = request.form['name']
#    location = request.form['location'] 
#    return f'<h1>Hi {name} from {location}, you have submitted the form successfully!</h1>'

# redirecting user
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''  <form method = "POST" action='/login'>
                        <input type= 'text' name= 'user'>
                        <input type= 'submit' value= 'Log in'>
                    </form>'''
    else:
        my_user = request.form['user']
        return redirect(url_for('home', name= my_user, location = 'NoLocation'))

#-----------------------------------------------------------------------------#
# calling the app
if __name__ == '__main__':
    app.run()

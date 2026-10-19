from flask import Flask, jsonify, request, g
from markupsafe import escape
import sqlite3

# app object instantiation
app = Flask(__name__)

#-----------------------------------------------------------------------------#
# database helping functions:
def connect_db():
    sql = sqlite3.connect('/home/myProjects/PythonLearning/9.Frameworks/Flask_Udemy/1.members_app/members.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr('g', 'sqlite_db'):
        g.sqlite_db.close()

#-----------------------------------------------------------------------------#
# [optional] user's basic authentication
users_dictionary = {
    'user1' : 'pass1',
    'user2' : 'pass2',
    'user3' : 'pass3'
}

# authenticator decorator function
def authenticator(fn):
    def wrapper(*args):
        auth = request.authorization
        if auth and auth.username in users_dictionary and auth.password == users_dictionary[auth.username]:
            return fn(*args)
        return jsonify({'message': 'Authentication failed'}), 401
    return wrapper

#-----------------------------------------------------------------------------#
# api routes endpoints:
@app.route('/member', methods = ['GET'])
@authenticator
def get_members():
    '''
    receiving just a request
    reponse should be all saved entries in database and status code
    '''
    # latching data from database
    db = get_db()
    member_cur = db.execute("SELECT * FROM members")
    buffer = []
    for member in member_cur.fetchall():
        buffer.append({'id': member['id'], 'user': member['user'], 'email': member['email'], 'level': member['level'] })
    # response
    reponse = jsonify({'members': buffer})
    reponse.status_code = 200
    return reponse

@app.route('/member', methods = ['POST'])
def add_member():
    '''
    receiving a json in request and posting it as a db entry
    reponse should be a copy of the saved entry and status code 
    '''
    # latching data from request's body
    new_member_data = request.get_json()
    user = new_member_data['user']
    email = new_member_data['email']
    level = new_member_data['level']
    # saving latched entry to database
    db = get_db()
    db.execute("INSERT INTO members (user, email, level) VALUES (?,?,?)", [user, email, level])
    db.commit()
    # latching recently saved entry from database
    member_cur = db.execute("SELECT id, user, email, level FROM members WHERE user = ?", [user])
    new_member = member_cur.fetchone()
    # reponse
    reponse = jsonify({'member' : {'id': new_member['id'], 'user': new_member['user'], 'email': new_member['email'], 'level': new_member['level'] }})
    reponse.status_code = 201
    return reponse

@app.route('/member/<int:id>', methods = ['Get'])
def get_member(id):
    '''
    receiving just a request with id
    reponse should be required saved entry in database and status code
    '''
    # latching entry from database
    db = get_db()
    member_cur = db.execute('SELECT * From members WHERE id = ?', [id])
    new_mamber = member_cur.fetchone()
    # reponse
    reponse = jsonify({'member' : {'id': new_mamber['id'], 'user': new_mamber['user'], 'email': new_mamber['email'], 'level': new_mamber['level'] }})
    reponse.status_code = 200
    return reponse

@app.route('/member/<int:id>', methods = ['PUT'])
def edit_member(id):
    '''
    receiving a json and id in request and putting (updating) it into a db entry
    reponse should be required saved entry in database and status code
    '''
    # latching data from request's body
    updated_member_data = request.get_json()
    user = updated_member_data['user']
    email = updated_member_data['email']
    level = updated_member_data['level']
    # saving latched entry to database
    db = get_db()
    db.execute("UPDATE members SET user = ?, email = ?, level = ? WHERE id = ?", [user, email, level, id])
    db.commit()
    # latching recently saved entry from database
    member_cur = db.execute("SELECT * FROM members WHERE id = ?", [id])
    updated_member = member_cur.fetchone()
    # response
    response = jsonify({'member' : {'id': updated_member['id'], 'user': updated_member['user'], 'email': updated_member['email'], 'level': updated_member['level'] }})
    response.status_code = 200
    return response

@app.route('/member/<int:id>', methods = ['DELETE'])
def delete_member(id):
    '''
    receiving just a request with id
    reponse should be required saved entry in database and status code
    '''
    # connecting to database and deleting entry
    db = get_db()
    db.execute('DELETE FROM members WHERE id = ?', [id])
    db.commit()
    # response
    response = jsonify({'message': 'member has been deleted'})
    response.status_code = 200
    return response

#-----------------------------------------------------------------------------#
# calling the app
if __name__ == '__main__':
    app.run(debug = True)

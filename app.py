from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
from connect import insertdb
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_random_secret_key'  # Update to a secure secret key
socketio = SocketIO(app)

# MySQL connection function
def get_db_connection():
    mysql.connector.connect(
    host="localhost",
    user="root",
    password="SAI123",  # ✅ Your actual password
    database="skillswap"
)

    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login1')
def login1():
    return render_template('login.html')

@app.route('/portal')
def portal():
    return render_template('portal.html')

@app.route('/reges')
def reges():
    return render_template('registration.html')

@app.route('/up')
def up():
    return render_template('userprofile.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        contact = request.form['mobile']
        address = request.form['address']
        role = "Faculty" if request.form['role'] == "0" else "Student"
        branch = request.form['branch']
        password = request.form['pwd']
        
        insertdb(name, email, contact, address, role, branch, password)
        return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pwd']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM USER WHERE email=%s AND password=%s"
        cursor.execute(sql, (email, password))
        userdetails = cursor.fetchone()
        if userdetails:
            session['register'] = userdetails["email"]
            return render_template('userprofile.html', 
                                   name=userdetails["name"], 
                                   email=userdetails["email"], 
                                   contact=userdetails["contact"], 
                                   address=userdetails["address"], 
                                   role=userdetails["role"], 
                                   branch=userdetails["branch"])
        else:
            msg = "Incorrect Email or Password"
            return render_template("login.html", msg=msg)
    return render_template('portal.html')

@app.route('/chat')
def chat():
    return render_template('chat.html', name=session.get('register'))

@socketio.on('send_message')
def handle_send_message(data):
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
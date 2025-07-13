import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="samskruthi@2005",
        database="skillswap"
    )
    return conn

def showall():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * from USER")
    rows = cursor.fetchall()
    for dictionary in rows:
        print("The Name is : ", dictionary["name"])
        print("The E-mail is : ", dictionary["email"])
        print("The Contact is : ", dictionary["contact"])
        print("The Address is : ", dictionary["address"])
        print("The Role is : ", dictionary["role"])
        print("The Branch is : ", dictionary["branch"])
        print("The Password is : ", dictionary["password"])
    cursor.close()
    conn.close()

def getdetails(email, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM USER WHERE email=%s AND password=%s"
    cursor.execute(sql, (email, password))
    dictionary = cursor.fetchone()
    if dictionary:
        print("The Name is : ", dictionary["name"])
        print("The E-mail is : ", dictionary["email"])
        print("The Contact is : ", dictionary["contact"])
        print("The Address is : ", dictionary["address"])
        print("The Role is : ", dictionary["role"])
        print("The Branch is : ", dictionary["branch"])
        print("The Password is : ", dictionary["password"])
    cursor.close()
    conn.close()

def insertdb(name, email, contact, address, role, branch, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO USER (name, email, contact, address, role, branch, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (name, email, contact, address, role, branch, password))
    conn.commit()
    cursor.close()
    conn.close()
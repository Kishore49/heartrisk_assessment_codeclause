# DB
import sqlite3
import threading

# Create a thread-local storage for SQLite connections
thread_local = threading.local()

# Function to get SQLite connection for the current thread
def get_connection():
    if not hasattr(thread_local, "connection"):
        thread_local.connection = sqlite3.connect('usersdata.db')
    return thread_local.connection

# Functions
def create_usertable():
    conn = get_connection()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
    conn.commit()

def add_userdata(username, password):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username, password):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

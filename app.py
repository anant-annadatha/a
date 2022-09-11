from functools import wraps
from http import client
from flask import Flask, redirect, render_template, session
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "b\xdc\xa0\x14\x7f6\xeb)\x97U\xb9S2\\\xdf\xa8\x15"

#Databases

cluster = MongoClient("mongodb+srv://DEMODOGS:DEMODOGS@demodogs-apad.4aejn.mongodb.net/?retryWrites=true&w=majority")
db2 = cluster["DFS_Customer"]
User_Preferences = db2["User_Preferences"]

# client = pymongo.MongoClient(app)
# db = client.users_table

# Login required functions (decorators)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

#Routes import
from user import routes

@app.route('/')
def home():
    return render_template('home1.html')

    
@app.route("/dashboard/")
@login_required
def hardware():

    id = session['User_Preferences']['dlplate']
    return render_template('dashboard1.html')   

if __name__ == '__main__':
    app.run(debug=True)
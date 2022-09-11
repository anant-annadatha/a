from crypt import methods
from flask import Flask
from app import app
from user.models import Recc

@app.route('/project/retrieve',methods = ['POST'])
def project_open():
    return Recc().Wheel()

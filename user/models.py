from datetime import datetime
from logging import log
from sqlite3 import Timestamp
from flask import Flask, jsonify, redirect, request, session
import uuid
from passlib.hash import pbkdf2_sha256
from app import dlplate, User_Preferences

class Recc:
    def start_session(self, dlplateinfo):
        session['logged_in'] = True
        session['dlfind'] = dlplateinfo
        return jsonify(dlplateinfo), 200

    def Wheel(self):
        dlplateinfo = request.form.get('dlplate')
        dlfind = dlplate.find_one( {"dlplate": dlplate } )
        if dlplate.find_one( {"dlplate": dlplate } ):
            return self.start_session(dlfind)
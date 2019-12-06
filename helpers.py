# Rafael Alejandro Valencia Ramos
# Final Project

import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

from flask_socketio import SocketIO, emit
# Configure application

def apology(message, code=400):

    def escape(s):

        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


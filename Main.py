import mysql.connector
import _thread
import Initialization
import MainUpdator
from Utilities import getInformation as info

Initialization.create(info.getDB(info),info.getPort(info))

def server( threadName ):
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()

_thread.start_new_thread( server, ("Thread-1", ) )

import GUI

print ("heh")
import _thread
import MainUpdator

u = MainUpdator.Updator()

def server( threadName ):
    from flask import Flask
    from flask import request
    print("run flask")
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"
    @app.route("/mehT")
    def helloMehT():
        return "Hello MehT!"

    @app.route("/login")
    def login():
        username = request.args.get('username')
        password = request.args.get('password')
        option = request.args.get('option')
        productID = request.args.get('productID')
        if(option == 'view'):
            pass
        elif(option == 'edit'):
            sensorType = request.args.get('SensorType')
            data = []
            for i in range(3):
                data.append(int(request.args.get('data'+str(i+1))))
        if(u.checkExistance(username)):
            if(u.checkUsername(username,password)):
                #if(u.checkOwnership(sensorType,productID,username)):
                    u.updateSensor(sensorType,productID,data[0] , data[1] , data[2])


        return "khar"

    #if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5004')

def runThread():
    _thread.start_new_thread( server, ("Thread-1", ) )
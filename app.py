from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')

def index():

    return "This is working From Daniel"
 
if __name__ == '__main__':

    app.run()   
 
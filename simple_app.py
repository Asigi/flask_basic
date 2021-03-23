
from flask import Flask
from flask import request #need to import this object to have access to the query strings.


#name app whatever the current namespace is
app = Flask(__name__)


@app.route('/')
@app.route('/<name>') #a view can have multiple routes, so this function will respond on multiple url endpoints. EX: http://0.0.0.0:8000/gill
def index(name="Arsh"): #Arsh is default name
    #name = request.args.get('name', name) #checks if given a name, else uses the default name above
        #note: arguments in the query string are not automatically converted to their native types.
    return "Hello from {}".format(name)
    
    
#route with multiple inputs. EX: http://0.0.0.0:8000/add/1/1
@app.route('/add/<int:num1>/<int:num2>') #whatever comes in gets turned into an int (entering a string will result in error b/c cant convert that)
@app.route('/add/<float:num1>/<float:num2>') #whatever comes in gets turned into a float.
@app.route('/add/<int:num1>/<float:num2>') #int, float
@app.route('/add/<float:num1>/<int:num2>') #float, int
def add(num1, num2):
    return '{} + {} = {}'.format(num1, num2, num1+num2)
    #note: flask can only return string, other type will cause error.


app.run(debug=True, port=8000, host='0.0.0.0')
#Note: dont need to rerun the program from console because debug=true. The program is auto-rerun whenever this code file is changed.


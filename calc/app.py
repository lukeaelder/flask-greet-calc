from flask import Flask , request
from operations import *
app = Flask(__name__)

@app.route("/add")
def math_add():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))

@app.route("/sub")
def math_sub():
    """Subtract a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.route("/mult")
def math_mult():
    """Multiply a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.route("/div")
def math_div():
    """Divide a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))

functions = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

@app.route("/math/<operator>")
def all_math(operator):
    """Perform given operation on a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(functions[operator](a,b))
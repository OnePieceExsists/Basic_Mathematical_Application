import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result) 

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)

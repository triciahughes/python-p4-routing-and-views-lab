#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(f'{string}')
    return f'{string}'

@app.route('/count/<int:integer>')
def count(integer):
    count = ''
    for i in range(integer):
        count += f'{i}\n'
    return count
    # return f'{integer}'

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    # solution = num1 + operation + num2
    # return solution
    # elif operation == '-':
    #     return num1 - num2
    if operation == "+":
        solution = num1 + num2
        return str(solution)
    elif operation == "-":
        solution = num1 - num2
        return str(solution)
    elif operation == "*":
        solution = num1 * num2
        return str(solution)
    elif operation == "div":
        solution = num1 / num2
        return str(solution)
    elif operation == "%":
        solution = num1 % num2
        return str(solution)
    
#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:num>')
def count(num):
    range_of_num = ''
    for n in range(0, num):
        print(f"{n}")
        range_of_num = range_of_num + str(n) + "\n"
    return range_of_num

@app.route("/math/<int:n1>/<string:operation>/<int:n2>")
def math(n1,operation,n2):
    result = 0
    if operation == "div":
        result = n1 / n2
    elif operation == "+":
        result =  n1 + n2
    elif operation == "-":
         result = n1 - n2
    elif operation == "*":
         result = n1 * n2
    else:
         result = n1 % n2
    return str(result)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)



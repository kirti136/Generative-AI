from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data_dict = {}

@app.route('/')
def welcome():
    return "Welcome to the Flask Greetings and Farewells App!"

@app.route('/greet/<username>')
def greet(username):
    return f"Hello, {username}!"

@app.route('/farewell/<username>')
def farewell(username):
    return f"Goodbye, {username}!"

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data_dict[key] = value
        print(data_dict)
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html', data_dict=data_dict)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        if key in data_dict:
            data_dict[key] = value
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data_dict:
            del data_dict[key]
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)

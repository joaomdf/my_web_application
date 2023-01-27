import os
from flask import Flask, request


app = Flask(__name__)
#curl http://localhost:5000/

@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'
    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name=request.form['name']
    message=request.form['message']

    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    return f'I am waving at {name}'

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text=request.form['text']
    count = 0
    for char in text:
        if char in 'aeiou':
            count += 1
    return f'There are {count} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def sort_names():
    if 'names' not in request.form:
        return "400 Bad Request", 400
    names=request.form['names']
    l = names.split(",")
    l.sort()
    sorted_names = ",".join(l)
    return sorted_names

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


import os
from flask import Flask, request


app = Flask(__name__)
# curl http://localhost:5000/names

# Initial challenge
# @app.route('/names')
# def get_add_name():
#     if 'add' not in request.args:
#         return 'Bad request!', 400
#     add = request.args['add']
#     preset = 'Julia, Alice, Karim'
#     if add == '':
#         return preset
#     return preset + ', ' + add

@app.route('/names')
def get_add_name():
    if 'add' not in request.args:
        return 'Bad request!', 400
    add = request.args['add']
    preset = 'Julia,Alice,Karim'
    if add == '':
        return ', '.join(sorted(preset.split(',')))

    all_names = preset + ',' + add
    split_add = all_names.split(',')
    split_add.sort()
    return ', '.join(split_add)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
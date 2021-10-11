from types import MethodDescriptorType
from model import LanguageModel

import json
# import csv
# import pickle
from flask import Flask, request
from flask_cors import CORS, cross_origin

# FLASK code
app = Flask(__name__)  # creating the Flask class object
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=['GET'])
def hello():
    data = {"key": "home page value"}
    data1 = json.dumps(data)
    return data1


# @app.route("/get", methods=['POST'])
# def pick():
#     input = request.json['name']

#     return input

'''The body of the POST request contains the input text'''


@app.route('/get', methods=['POST'])
def fun():
    res = LanguageModel.pickup_line_gen()
    return res


@app.route('/seg', methods=['POST'])
def fun1():
    res = request.json['name']
    data = {"key": res}
    data1 = json.dumps(data)
    return data1

# input_text = "Lauren 36, Visual artist and freelance costume/set designer. Former international ballroom dancer"
# ans = pickup_line_gen(input_text)
# print("ans: ", ans)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)

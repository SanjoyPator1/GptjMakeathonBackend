from types import MethodDescriptorType
from GPTJ.gptj_api import Completion

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
def pickup_line_gen():

    context = "Pickup line for tinder profiles"

    examples = {
        "Lauren 36, Visual artist and freelance costume/set designer. Former international ballroom dancer":
            "Hey are you an artist? Because you sure do draw my attention ;)",
        "Leanne 28, Reader, writer, maker, and educator": "Babe, if you were words on a page, you'd be what they call fine print.",
        "Tess 23, Cat Enthusiast. Human, mostly.": "If I were a cat, I'd spend all nine lives with you.",
    }

    context_setting = Completion(context, examples)

    prompt = request.json['name']

    User = "Girl"
    Bot = "Guy"

    max_tokens = 20

    temperature = 0.4

    top_probability = 1.0

    response = context_setting.completion(prompt,
                                          user=User,
                                          bot=Bot,
                                          max_tokens=max_tokens,
                                          temperature=temperature,
                                          top_p=top_probability)

    res = {"res ": response}

    # # print(featureCollection)
    json_obj = json.dumps(res)

    return json_obj


# input_text = "Lauren 36, Visual artist and freelance costume/set designer. Former international ballroom dancer"
# ans = pickup_line_gen(input_text)
# print("ans: ", ans)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)

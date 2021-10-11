import json
from flask import request
from GPTJ.gptj_api import Completion
import random


class LanguageModel:

    def __init__(self):
        pass

    @classmethod
    def pickup_line_gen(cls, context="This is a bot that will create love letters",
                        examples={"Lauren 36, Visual artist and freelance costume/set designer. Former international ballroom dancer": "Hey are you an artist? Because you sure do draw my attention)",
                                  "Leanne 28, Reader, writer, maker, and educator": "Babe, if you were words on a page, you'd be what they call fine print.",
                                  "Tess 23, Cat Enthusiast. Human, mostly.": "If I were a cat, I'd spend all nine lives with you."}):

        context_setting = Completion(context, examples)

        prompt = request.json['name']

        User = "Girl"
        Bot = "Guy"

        max_tokens = 25

        temperature = 0.2

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

    @classmethod
    def automated_pickup(cls):
        lines = open("result.json")
        lines = json.load(lines)

        keyword = request.json['keyword']

        print(type(keyword))
        print(keyword)

        # return keyword

        if keyword in lines.keys():
            res = {"res ": random.choice(lines[keyword])}
            return json.dumps(res)
        else:
            res = {"res ": random.choice(lines['general'])}
            return json.dumps(res)

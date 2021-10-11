import json
from flask import request
from GPTJ.gptj_api import Completion
import random


class LanguageModel:

    def __init__(self):
        pass

    @classmethod
    def pickup_line_gen(cls, context="This is a bot that will create love letters",
                        examples={
                            "General": "If kisses were snowflakes, I'd send you a blizzard.",
                            "Math": "My love for you is like the slope of a concave up function because it is always increasing.",
                            "Engineer": "Damn girl you must be a strong magnetic field because you just induced a flow somewhere in me.",
                            "music": "What has a differential of zero and has no concavity? My love for you, because it's constant.",
                            "classic": "Kissing is a language of love, so how about a conversation?",
                            "Sport": "I don't know if its this workout or you that just took my breath away.",
                            "Sport": "I bet you play soccer because you're a keeper.",
                            "Running": "Do you believe in love at first sight or do I need to run around this track again?",
                            "Star Trek": "Hey baby, are your hailing frequencies open?",
                            "Star Wars": "You’re hotter than the flames on Mustafar",
                            "Travel": "Are you a cartographer? Because you have mileage markers in all the righTwt places.",
                            "Cats": "If I were a cat, I'd spend all 9 lives with you",
                            "Animals": "Tell me what makes you purrr"}):

        context_setting = Completion(context, examples)

        prompt = request.json['name']

        User = "Partner"
        Bot = "Romeo"
        max_tokens = 80
        temperature = 0.7
        top_probability = 0.85

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

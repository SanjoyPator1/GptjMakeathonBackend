import json
from flask import request
from GPTJ.gptj_api import Completion


class LanguageModel:

    def __init__(self):
        pass

    @classmethod
    def pickup_line_gen(cls, context="Pickup line for tinder profiles",
                        examples={"Lauren 36, Visual artist and freelance costume/set designer. Former international ballroom dancer": "Hey are you an artist? Because you sure do draw my attention)",
                                  "Leanne 28, Reader, writer, maker, and educator": "Babe, if you were words on a page, you'd be what they call fine print.",
                                  "Tess 23, Cat Enthusiast. Human, mostly.": "If I were a cat, I'd spend all nine lives with you."}):

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

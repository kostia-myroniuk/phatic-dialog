from helper.engine import AnswerEngine
import codecs


with codecs.open('helper/templates.txt', 'r', 'utf-8') as templates_responses:
    templates = []
    for template in templates_responses.readlines():
        templates.append(tuple(template.split('|')))
    engine = AnswerEngine(templates)

    # message = input()
    # print(engine.create_answer(message))

def resp(mes):
    return engine.create_answer(mes)

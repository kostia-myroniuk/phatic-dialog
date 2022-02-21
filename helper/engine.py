import re
import random

class AnswerEngine:
    def __init__(self, templates):
        self.templates = templates
        self.template_answers = [answer for (template, answer) in templates if template == '*']

    def parse_template(self, template, question, answer):
        if template.find("*") != -1:
            template = template.replace("*", "")

            if not template:
                return answer
            if len(template) == 1 and question.find(template) != -1 and answer.find(template) != -1:
                return answer

        if template.find("<c>") != -1:
            template = template.replace("<c>", "")
            pattern = re.compile(rf"((?:{template}\s))(\w+)")
            match = pattern.search(question)
            if match is None:
                return None
            match = match.group(0).replace(template, "").strip()
            return answer.replace("<c>", match)

        return answer if question.find(template) != -1 else None


    def create_answer(self, question):
        question = question.lower()
        
        answers = []
        for (template, answer) in self.templates:
            result = self.parse_template(template, question, answer)
            if result is not None:
                answers.append(result)

        if len(answers) > len(self.template_answers):
            answers = [answer for answer in answers if answer not in self.template_answers]

        return answers[random.randint(0, len(answers)-1)]

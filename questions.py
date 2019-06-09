from __future__ import print_function, unicode_literals

from PyInquirer import prompt
import yaml
import os
from sys import platform


def _load_yml():
    with open("./questions.yml", 'r') as ymlfile:
        yml = yaml.safe_load(ymlfile)
    return yml


def _load_title(topic):
    questions_conf = _load_yml()

    q_topic = questions_conf[topic]
    return q_topic['title']


def _load_questions(topic, optional=None):
    questions_conf = _load_yml()

    q_topic = questions_conf[topic]

    startup_questions = []
    if q_topic['questions'] is not None:
        for q in q_topic['questions']:
            startup_questions.append({'name': q['question']})

    # append optional questions
    if optional is not None:
        for q in optional:
            startup_questions.append({'name': q})

    return startup_questions


def _build_question(q_type, topic, optional_questions):
    choices = _load_questions(topic, optional_questions)
    question = _load_title(topic)

    return [{
        'type': q_type,
        'qmark': '💻',
        'message': question,
        'name': topic,
        'choices': choices
    }]


def _clear_console():
    if platform == 'win32' or platform == 'cygwin':
        os.system('cls')
    else:
        os.system('clear')


def _get_module_by_answer(topic, answer):
    yml = _load_yml()
    yml_topic = yml[topic]
    questions = yml_topic['questions']

    # let's check if there's a configured answer and what module we need next
    if questions is not None:
        for q in questions:
            q_obj = {topic: q['question']}
            if answer == q_obj:
                return q['module']

    # ok, so if there's no configured answer, lets check if we got a general next module
    module = yml_topic['module']
    if module is not None:
        return module

    # ok we have nothing, so return None as default
    print("Found nothing")
    return None


def list(topic, optional_questions=None, clear_console=False):
    if clear_console:
        _clear_console()

    q = _build_question('list', topic, optional_questions)
    answer = prompt(q)

    module = _get_module_by_answer(topic, answer)
    selection = answer[topic]
    return module, selection


def select(topic, optional_questions=None, clear_console=False):
    if clear_console:
        _clear_console()

    q = _build_question('checkbox', topic, optional_questions)
    answer = prompt(q)

    module = _get_module_by_answer(topic, answer)
    selection = answer[topic]
    return module, selection

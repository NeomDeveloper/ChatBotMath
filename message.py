import IPython
from IPython.display import clear_output, HTML, display
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
import time
import json

interpreter = RasaNLUInterpreter('models/nlu')
messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
agent = Agent.load('models/', interpreter=interpreter)


def chatlogs_html(messages):
    messages_html = "".join(["<p>{}</p>".format(m) for m in messages])
    chatbot_html = """<div class="chat-window" {}</div>""".format(messages_html)
    return chatbot_html


while True:
    clear_output()
    display(HTML(chatlogs_html(messages)))
    time.sleep(0.3)
    a = input()
    messages.append(a)
    print(messages)
    if a == 'stop':
        break
    responses = agent.parse_message_using_nlu_interpreter(a)
    print(json.dumps(responses))

    # for r in responses:
    #     messages.append(r.get("text"))

from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-804949982787-808509426721-818714468918-b31f56eee568a0cdc8e90f83e2ea7a2f', #app verification token
							'xoxb-804949982787-816513010133-Q3DBRRARFpceLjnxRoPFhaWF', # bot verification token
							'rJgaKGknViGjv3fvldujGMKX', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))

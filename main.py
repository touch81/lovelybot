__metaclass__ = type

from microsoftbotframework import MsBot
from tasks import *
import os

#bot = MsBot(port=int(os.environ['PORT']))
bot = MsBot()
bot.add_process(echo_response)
#bot.run()
bot.run(port=int(os.environ['PORT']))

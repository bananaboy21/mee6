from mee6 import Mee6
import os
import logging

token = os.getenv('MEE6_TOKEN')
redis_url = os.getenv('REDIS_URL')
mongo_url = os.getenv('MONGO_URL')
mee6_debug = os.getenv('MEE6_DEBUG')
if mee6_debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

bot = Mee6(redis_url=redis_url, mongo_url=mongo_url)
bot.run(token)

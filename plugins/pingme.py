# imports
from . import * #import at modular level
import time


@start.on_message(filters.command("ping", ".")) #command
async def ping(msg: Message):
  start = time.time()
  end = time.time()
  ms = start - end / 1000
  
  await start.send_message(msg.chat.id, "PONG")
  await msg.edit("I am on with Ms: {}").format(ms) #result

import os
from pyrogram import Client


API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
TOKEN = os.environ.get("TOKEN", "")
SESSION = os.environ.get("SESSION", "")

start = Client(
  name = "[MUSIC CLIENT]",
  api_id = API_ID,
  api_hash = API_HASH,
  string_session = SESSION,
  plugins = {"root": "plugins"}
)

asst = Client(
  name = "[MUSIC ASSISTANT]",
  api_id = API_ID,
  api_hash = API_HASH,
    bot_token = TOKEN,
  plugins = {"root": "plugins"}
)

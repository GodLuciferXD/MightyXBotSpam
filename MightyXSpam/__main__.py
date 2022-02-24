# FlashXSpamBot || @Flash_Support_Group

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from FlashXSpamBot.utils import load_plugins
import logging
from telethon import events
from . import Fla, Fla2, Fla3, Fla4, Fla5, Fla6, Fla7, Fla8, Fla9, Fla10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "FlashXSpamBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("😈😈😈💣💣 Flash X SPAM BOT BAN GYA JAAO MOJ KARO BACHO 😈😈� !!")
print("Enjoy! Do Visit @Flash_Support_Group")

if __name__ == "__main__":
    Fla.run_until_disconnected()
    
if __name__ == "__main__":
    Fla2.run_until_disconnected()

if __name__ == "__main__":
    Fla3.run_until_disconnected()
    
if __name__ == "__main__":
    Fla4.run_until_disconnected()

if __name__ == "__main__":
    Fla5.run_until_disconnected()
    
if __name__ == "__main__":
    Fla6.run_until_disconnected()
    
if __name__ == "__main__":
    Fla7.run_until_disconnected()

if __name__ == "__main__":
    Fla8.run_until_disconnected()
    
if __name__ == "__main__":
    Fla9.run_until_disconnected()

if __name__ == "__main__":
    Fla10.run_until_disconnected()    

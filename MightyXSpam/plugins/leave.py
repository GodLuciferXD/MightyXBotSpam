import asyncio
from FlashyXSpam import Fla, Fla2, Fla3, Fla4, Fla5, Fla6, Fla7, Fla8, Fla9, Fla10, SUDO_USERS
from FlashyXSpam import CMD_HNDLR as hl
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
import os
import random
import sys

@Fla.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        flashy = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = flashy[0]
            Xd = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(Xd))
                await event.edit("FINALLY NIKAL GYA GROUP SE ✅")
            except Exception as e:
                await event.edit(str(e))
         
        else:
             bc = e.chat_id
             Xd = int(bc)
             text = "BHKK BC KOI V CHUTIYE GROUP ME ADD LAR DETE KOI NA KRISHNA SIR "
             if e.is_private:
                  dik = f"You Can't Do This Here !! \n\n {hl}leave <Channel or Chat ID> \n {hl}leave : type in the group bot will auto leave that group !"
                  await e.reply(dik, parse_mode=None, link_preview=None )
             else:
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  try:
                      await event.client(LeaveChannelRequest(Xd))
                  except Exception as e:
                      await event.edit(str(e))

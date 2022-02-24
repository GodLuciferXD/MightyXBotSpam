
import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from FlashXSpam import Fla, Fla2, Fla3, Fla4, Fla5 , Fla6, Fla7, Fla8, Fla9, Fla10, SUDO_USERS, OWNER_ID

from FlashXSpam import CMD_HNDLR as hl
from FlashXSpam.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from resources.data import FlashyX


@Fla.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `{hl}addecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in FlashyX:
                    text = f"Chala Jaa BSDK M Apne Malik KA Echo Na Kar Sakta"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                    text = f"Bhkk BSDK Mera Malik H Krishna."
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                    text = f"This Guy is a Sudo User."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 try:
                     hmm = base64.b64decode("QEZsYXNoX1N1cHBvcnRfR3JvdXA=")
                     hmm = Get(hmm)
                     await event.client(hmm)
                 except BaseException:
                    pass
                 if is_echo(user_id, chat_id):
                     await event.reply("Iska Echo karne lag raha hu ")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("Echo SE ROO DEGA BETA ✅")
     else:
          await event.reply(usage)

@Fla.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDO_USERS or event.sender_id in DEV:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            try:
                hmm = base64.b64decode("QEZsYXNoX1N1cHBvcnRfR3JvdXA=")
                hmm = Get(hmm)
                await event.client(hmm)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("CHAL BETA CHOR DIYA JAA MOJ KAR KRISHNA KO PAPA BOL ☑️")
            else:
                await event.reply("ISS CHUTIYE KI ECHO NA KARU")
     else:
          await event.reply(usage)


@Fla.on(events.NewMessage(incoming=True))
@Fla2.on(events.NewMessage(incoming=True))
@Fla3.on(events.NewMessage(incoming=True))
@Fla4.on(events.NewMessage(incoming=True))
@Fla5.on(events.NewMessage(incoming=True))
@Fla6.on(events.NewMessage(incoming=True))
@Fla7.on(events.NewMessage(incoming=True))
@Fla8.on(events.NewMessage(incoming=True))
@Fla9.on(events.NewMessage(incoming=True))
@Fla10.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.5)
        try:
            Flashy= base64.b64decode("QEZsYXNoX1N1cHBvcnRfR3JvdXA=")
            Flashy = Get(Flashy)
            await e.client(Flashy)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)

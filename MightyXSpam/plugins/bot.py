import os
import asyncio
import sys
import git
import heroku3
from FlashXSpamBot import Fla, Fla2, Fla3, Fla4, Fla5 , Fla6, Fla7, Fla8, Fla9, Fla10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, flashyversion
from FlashXSpamBot import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from FlashXSpamBot import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

MIG_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/bb8fd844194361ffea7e5.jpg"
  

flashy = "╚»★ ғʟᴀsʜxsᴘᴀᴍʙᴏᴛ 𝗶𝘀 𝗛𝗲𝗿𝗲 ★«╝\n\n"
flashy += f"═══════════════════\n"
flashy += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"
flashy += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
flashy += f"• **ғʟᴀsʜxsᴘᴀᴍʙᴏᴛ ᴠᴇʀsɪᴏɴ**  : `{flashyversion}`\n"
flashy += f"═══════════════════\n\n"   

                                  
@Fla.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  FLA_PIC,
                                  caption=mighty,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Flash_Updates"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Flash_Support_Group")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Alcoholic-Krish/FlashXSpamBot")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Fla.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Hᴍᴍᴍ Mᴇ Zɪɴᴅᴀ  Hᴜ ᴅᴇᴋʜᴏɢᴇ Pɪɴɢ Pᴏɴɢ Tɪɴɢ Tᴏɴɢ ɢɪʟʟɪ Gɪʟʟɪ Cʜᴜᴜ👻👻!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\nϟ Fʟᴀsʜ X Sᴘᴀᴍ ϟ︎ `{fs}` ғs")
        

@Fla.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "Cʜᴀʟᴏ Aʙ ᴊᴀᴀᴋʀ  Sᴏ ᴊᴀᴛᴀ ʜᴜ Bʏᴇ Bʏᴇ... | Please Wait Few Hours Lmao majak tha bhai kar lena use 2min baad."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Fla.disconnect()
        except Exception:
            pass
        try:
            await Fla2.disconnect()
        except Exception:
            pass
        try:
            await Fla3.disconnect()
        except Exception:
            pass
        try:
            await Fla4.disconnect()
        except Exception:
            pass
        try:
            await Mig5.disconnect()
        except Exception:
            pass
        try:
            await Fla6.disconnect()
        except Exception:
            pass
        try:
            await Fla7.disconnect()
        except Exception:
            pass
        try:
            await Fla8.disconnect()
        except Exception:
            pass
        try:
            await Fla9.disconnect()
        except Exception:
            pass
        try:
            await Fla10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@Fla.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding User As Sudo...")
         flashy = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply To a User.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** As Sudo User ✨ || Restarting... Please Wait Few Seconds.")
        heroku_var[flashy] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target

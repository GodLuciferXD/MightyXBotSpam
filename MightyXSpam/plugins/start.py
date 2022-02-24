import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Fla, Fla2, Fla3, Fla4, Fla5, Fla6, Fla7, Fla8, Fla9, Fla10, ALIVE_PIC, OWNER_ID
from FlashXSpamBot.plugins.help import *


Fla_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/bb8fd844194361ffea7e5.jpg"

Fla_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/@Flash_Support_Group")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
FlaX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Flash_Updates"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Flash_Support_Group")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Alcoholic-Krish/FlashXSpamBot")
        ]
        ]
        
        
#USERS 


@Fla.on(events.NewMessage(pattern="/start"))
@Fla2.on(events.NewMessage(pattern="/start"))
@Fla3.on(events.NewMessage(pattern="/start"))
@Fla4.on(events.NewMessage(pattern="/start"))
@Fla5.on(events.NewMessage(pattern="/start"))
@Fla6.on(events.NewMessage(pattern="/start"))
@Fla7.on(events.NewMessage(pattern="/start"))
@Fla7.on(events.NewMessage(pattern="/start"))
@Fla8.on(events.NewMessage(pattern="/start"))
@Fla9.on(events.NewMessage(pattern="/start"))
@Fla10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       MigBot = await event.client.get_me()
       bot_id = FlaBot.first_name
       bot_username = FlaBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheFlashy = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hello Chacha !!, Its Me {bot_id}, Your Bot Banya hu Krishna ne  !! \n\n Click Below Buttons For Help. 🌚**"
       usermsg = f"**Hey !! {firstname} ! Nice To Meet You, Well I Am {bot_id}, A Powerfull Spam Bot Made By My Real Owner Krishna and Jisko dm Kiya wo fake h.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**Powered By : [Fʟᴀsʜ X](https://t.me/Flash_Support_Group)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheFlashy,
                  FLA_IMG,
                  caption=ownermsg, 
                  buttons=Fla_Button)
       else:
            await event.client.send_file(TheFlashy,
                  FLA_IMG,
                  caption=usermsg, 
                  buttons=FLAX_Button)
                


from FlashXSpam import Fla, Fla2, Fla3, Fla4, Fla5, Fla6, Fla7, Fla8, Fla9,  Fla10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from FlashXSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/ea225d8d3d9cb0abf9f32.jpg"

Fla_Help = "__Click On Below Buttons For Help__"


@Fla.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Mig_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Flash_Updates")
           ],
           [
           Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Flash_Support_Group")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: Userbot Cmds
Command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> || Owner Cmd ||

**Echo**: To Active Echo On Any User
Command:
i) {hl}addecho <reply to user>
ii) {hl}rmecho <reply to user>

**Leave**: To Leave Group/Channel
Command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group

**Packspam**: Sticker Pack Spam
i) {hl}packspam (replying to any sticker)

**© @Flash_Support_Group**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**Raid:** Activates Raid on Any individual User For Given Range.
Command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>

**Delayraid**: Activates Raid on Any individual User For Given Range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**ReplyRaid:** Activates Reply Raid on The User!!
Command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**DReplyRaid:** Deactivates Reply Raid on The User!!
Command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @Flash_Support_Group**
"""

spam_msg = f"""
**Help Spam Cmds**

**Spam**: Spams a Message For Given Counter(<= 100).
Command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**Bigspam**: Spams a Message For Given Counter.
Command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**Delayspam**: Delay Spam a Text For Given Counter After Given Time.
Command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**Pornspam**: Pornography Spam.
Command:
i) {hl}pornspam <count>

**Hang**: Spams Hanging Message For Given Counter.
Command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @Flash_Support_Group**
"""                     
           
           
@Fla.on(events.CallbackQuery(pattern=r"help_back"))
@Fla2.on(events.CallbackQuery(pattern=r"help_back"))
@Fla3.on(events.CallbackQuery(pattern=r"help_back"))
@Fla4.on(events.CallbackQuery(pattern=r"help_back"))
@Fla5.on(events.CallbackQuery(pattern=r"help_back"))
@Fla6.on(events.CallbackQuery(pattern=r"help_back"))
@Fla7.on(events.CallbackQuery(pattern=r"help_back"))
@Fla8.on(events.CallbackQuery(pattern=r"help_back"))
@Fla9.on(events.CallbackQuery(pattern=r"help_back"))
@Fla10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
           Fla_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/MightyXUpdates")
           ],
           [
           Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/MightyXSupport")
           ],
           ],
        )           
   else:
        Alert = (
                "BSDK JAAKE KUDH KA BANA DUSARO KA USE KARTA GANDU 👿👿 @Flash_Support_Group"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Fla.on(events.CallbackQuery(pattern=r"spam")) 
@Fla2.on(events.CallbackQuery(pattern=r"spam")) 
@Fla3.on(events.CallbackQuery(pattern=r"spam")) 
@Fla4.on(events.CallbackQuery(pattern=r"spam")) 
@Fla5.on(events.CallbackQuery(pattern=r"spam")) 
@Fla6.on(events.CallbackQuery(pattern=r"spam")) 
@Fla7.on(events.CallbackQuery(pattern=r"spam")) 
@Fla8.on(events.CallbackQuery(pattern=r"spam")) 
@Fla9.on(events.CallbackQuery(pattern=r"spam")) 
@Fla10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "BSDK JAAKE KUDH KA BANA DUSARO KA USE KARTA GANDU 👿👿 @Flash_Support_Group"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Fla.on(events.CallbackQuery(pattern=r"raid"))
@Fla2.on(events.CallbackQuery(pattern=r"raid"))
@Fla3.on(events.CallbackQuery(pattern=r"raid"))
@Fla4.on(events.CallbackQuery(pattern=r"raid"))
@Fla5.on(events.CallbackQuery(pattern=r"raid"))
@Fla6.on(events.CallbackQuery(pattern=r"raid"))
@Fla7.on(events.CallbackQuery(pattern=r"raid"))
@Fla8.on(events.CallbackQuery(pattern=r"raid"))
@Fla9.on(events.CallbackQuery(pattern=r"raid"))
@Fla10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "BSDK JAAKE KUDH KA BANA DUSARO KA USE KARTA GANDU 👿👿 @Flash_Support_Group"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Fla.on(events.CallbackQuery(pattern=r"extra"))
@Fla2.on(events.CallbackQuery(pattern=r"extra"))
@Fla3.on(events.CallbackQuery(pattern=r"extra"))
@Fla4.on(events.CallbackQuery(pattern=r"extra"))
@Fla5.on(events.CallbackQuery(pattern=r"extra"))
@Fla6.on(events.CallbackQuery(pattern=r"extra"))
@Fla7.on(events.CallbackQuery(pattern=r"extra"))
@Fla8.on(events.CallbackQuery(pattern=r"extra"))
@Fla9.on(events.CallbackQuery(pattern=r"extra"))
@Fla10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "BSDK JAAKE KUDH KA BANA DUSARO KA USE KARTA GANDU 👿👿 @Flash_Support_Group"
            )
        await event.answer(Alert, cache_time=0, alert=True)


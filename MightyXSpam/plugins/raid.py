
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from FlashyXSpam import Fla, Fla2, Fla3, Fla4, Fla5 , Fla6, Fla7, Fla8, Fla9, Fla10, SUDO_USERS, OWNER_ID
from resources.data import RAID, REPLYRAID, FlashyX
from FlashyXSpam import CMD_HNDLR as hl


que = {}


@Fla.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl)) 
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl)) 
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl)) 
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl)) 
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl)) 
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl)) 
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl)) 
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl)) 
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl)) 
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}raid <count> <Username of User>\n\n{hl}raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Flashy = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Flashy) == 2:
            user = str(Flashy[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in FlashyX:
                text = f"BSDK MERE HI MALIK PE RAID KAREGA RUK BSDK TERI GAND ME RAID KARTA RUK"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"BSDK YEH MASTER H MERA KRISHNA SAMJHA GAND KE MARIJ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Flashy[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in FlashyX:
                text = f"BSDK MERE HI MALIK PE RAID KAREGA RUK BSDK TERI GAND ME RAID KARTA RUK"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"BSDK YEH MASTER H MERA KRISHNA SAMJHA GAND KE MARIJ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo us6er."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Flashy[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



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
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@Fla.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}replyraid <Username of User>\n\n{hl}replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Flashy = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Migx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Flashy[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in FlashyX:
                text = f"BSDK MERE HI MALIK PE RAID KAREGA RUK BSDK TERI GAND ME RAID KARTA RUK."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"BSDK YEH MASTER H MERA KRISHNA SAMJHA GAND KE MARIJ."            
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"CHUDEGA BETA AB TU LIKH KE DIKHA 🤬🤬"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in FlashyX:
                text = f"BSDK MERE HI MALIK PE RAID KAREGA RUK BSDK TERI GAND ME RAID KARTA RUK."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"BSDK YEH MASTER H MERA KRISHNA SAMJHA GAND KE MARIJ."
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"CHUDEGA BETA AB TU LIKH KE DIKHA 🤬🤬"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@Fla.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl)) 
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl)) 
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl)) 
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl)) 
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl)) 
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl)) 
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl)) 
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl)) 
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl)) 
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n{hl}dreplyraid <Username of User>\n\n{hl}dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Migoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Migoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "JAA BETA CHOR DIYA KRISHNA PAPA NE TEKO MOJ KAR🥱🥱"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "JAA BETA CHOR DIYA KRISHNA PAPA NE TEKO MOJ KAR🥱🥱"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
@Fla.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Fla2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Fla3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Fla4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Fla5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Fla6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Fla7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Fla8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Fla9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@Fla10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
async def _(event):
   usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗘𝗟𝗔𝗬𝗥𝗔𝗜𝗗\n\nCommand:\n\n{hl}delayraid <delay> <count> <Username of User>\n\n{hl}delayraid <delay> <count> <reply to a User>\n\nCount and Sleeptime must be a integer."        
   if event.sender_id in SUDO_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         Mighty = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(Flashy) == 3:
             user = str(Flashy[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in FlashyX:
                    text = f"BSDK MERE HI MALIK PE RAID KAREGA RUK BSDK TERI GAND ME RAID KARTA RUK"
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) == OWNER_ID:
                text = f"BSDK YEH MASTER H MERA KRISHNA SAMJHA GAND KE MARIJ."
                await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SUDO_USERS:
                    text = f"This Guy is a Sudo User."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(Flashy[1])
                 sleeptimet = sleeptimem = float(Flashy[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in FlashyX:
                       text = f"BSDK MERE HI MALIK PE RAID KAREGA RUK BSDK TERI GAND ME RAID KARTA RUK"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) == OWNER_ID:
                       text = f"BSDK YEH MASTER H MERA KRISHNA SAMJHA GAND KE MARIJ."
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SUDO_USERS:
                       text = f"This Guy is a Sudo User."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Flashy[0])
                   counter = int(Flashy[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from files import UPDATE_CHANNEL

Motechyt = Client(
            "MT ID BOT",
            bot_token = os.environ["BOT_TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"]
)

# start and Update channel added
@Motechyt.on_message(filters.private & filters.command("start"))
async def start(motech, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("π Sorry Dude, You are **π±οΈπ°οΈπ½οΈπ½οΈπ΄οΈπ³οΈ π**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text="<b>π’ JOIN MY UPDATE CHANNEL π’</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" π’ πΉπππ πΌπ’ πππππππ π²ππππππ π’ ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"π’Add This Channel @{UPDATE_CHANNEL}")
            return  

    text = f"""
<b> πHello {update.from_user.mention}</b>

<b>I CAN GET ANY PUBLIC AND PRIVATE CHANNEL ID

FORWARD A MESSAGE FROM YOUR CHANNEL TO GET YOUR CHANNEL ID.

CLICK /ID GET YOUR ID

CLICK /INFO GET YOUR TELEGRAM INFO </b>
"""
    reply_markup =  MT_START
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

# Button Controler 
MT_START = InlineKeyboardMarkup(
     [[
        InlineKeyboardButton("Group", url=f"t.me/NAZRIYAOFFTOPIC"),
        InlineKeyboardButton("UPDATES", url=f"t.me/NAZRIYAONTOPIC"),
        InlineKeyboardButton("MASTER", url=f"t.me/SMILE_KILLER_010")
     ]]
   )

# telegram information from motech.py
@Motechyt.on_message(filters.private & filters.command("info"))
async def info(motech, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("π Sorry Dude, You are **π±οΈπ°οΈπ½οΈπ½οΈπ΄οΈπ³οΈ π**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text="<b>π’ JOIN MY UPDATE CHANNEL π’</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" π’ πΉπππ πΌπ’ πππππππ π²ππππππ π’ ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"π’Add This Channel @{UPDATE_CHANNEL}")
            return 

    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "Noneπ₯²"
    text = f"""
<b>ππ»ββοΈ First Name :</b> {update.from_user.first_name}

<b>π§ββοΈ Second Name :</b> {last_name}

<b>π§π»βπ Username :</b> @{update.from_user.username}

<b>π Telegram ID :</b> <code>{update.from_user.id}</code>

<b>π Profile Link :</b> {update.from_user.mention}

<b>  Β© @NAZRIYAOFFTOPIC.</b>
""" 
    reply_markup = MT_START 
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Motechyt.on_message(filters.private & filters.command("id"))
async def id(motech, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("π Sorry Dude, You are **π±οΈπ°οΈπ½οΈπ½οΈπ΄οΈπ³οΈ π**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text="<b>π’ JOIN MY UPDATE CHANNEL π’</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" π’ πΉπππ πΌπ’ πππππππ π²ππππππ π’ ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"π’Add This Channel @{UPDATE_CHANNEL}")
            return 

    text = f"""
π Your Telegram ID : <code>{update.from_user.id}</code>
"""
    reply_markup = MT_START
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

# Forwarded message id from motech.py
@Motechyt.on_message(filters.private & filters.forwarded)
async def forwarded(motech, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await msg.reply_text("π Sorry Dude, You are **π±οΈπ°οΈπ½οΈπ½οΈπ΄οΈπ³οΈ π**")
               return
        except UserNotParticipant:
            #await msg.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await msg.reply_text(
                text="<b>π’ JOIN MY UPDATE CHANNEL π’</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" π’ πΉπππ πΌπ’ πππππππ π²ππππππ π’ ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await msg.reply_text(f"π’Add This Channel @{UPDATE_CHANNEL}")
            return 
    if msg.forward_from:
        text = "<b>π€«Forward Informationπ€«</b> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<b>π€Bot</b>"
        else:
            text += "<b>π€User</b>"
        text += f'\nnπ¨βπΌName{msg.forward_from["first_name"]} \n'
        if msg.forward_from["username"]:
            text += f'\nπ UserName : @{msg.forward_from["username"]} \n\nπ ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\nπ ID : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"βοΈERROR {hidden} βοΈERROR",
                quote=True,
            )
        else:
            text = f"<b>Forward Informationπ</b>."
            if msg.forward_from_chat["type"] == "channel":
                text += "\n\n<b>π’ Channel</b>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "\n\n<b>π£οΈ Group</b>\n\n"
            text += f'π Name\n{msg.forward_from_chat["title"]} \n\n'
            if msg.forward_from_chat["username"]:
                text += f'<b>β‘οΈ From</b> : @{msg.forward_from_chat["username"]} \n\n'
                text += f'<b>π ID</b> : `{msg.forward_from_chat["id"]}`\n\n'
            else:
                text += f'<b>π ID</b> `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
     
# Sticker ID WOULD GET COPYRIGHT UNDER AND RE GENERATED AND MODED BY @MR-JINN-OFTG
@Motechyt.on_message(filters.private & ~filters.forwarded & ~filters.command(["start", "about", "help", "id"]))
async def stickers(motech, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await update.reply_text("π Sorry Dude, You are **π±οΈπ°οΈπ½οΈπ½οΈπ΄οΈπ³οΈ π**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await msg.reply_text(
                text="<b>π’ JOIN MY UPDATE CHANNEL π’</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" π’ πΉπππ πΌπ’ πππππππ π²ππππππ π’ ", url=f"t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return

    if msg.sticker:
        await msg.reply(f"This Sticker's ID is `{msg.sticker.file_id}`", quote=True)
    else:
        await msg.reply(f"Your Telegram ID is : `{msg.from_user.id}`")       
Motechyt.run()

    

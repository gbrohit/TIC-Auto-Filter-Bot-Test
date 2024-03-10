#Dont copy my codes u stupid 😂
import logging
import os
import requests
from pyrogram import Client, filters


@Client.on_message(filters.command('repo'))
async def git(Kashmira, message):
    pablo = await message.reply_text("`ᴘʀᴏᴄᴇssɪɴɢ...`")
    args = message.text.split(None, 1)[1]
    if len(message.command) == 1:
        await pablo.edit("No input found")
        return
    r = requests.get("https://api.github.com/search/repositories", params={"q": args})
    lool = r.json()
    if lool.get("total_count") == 0:
        await pablo.edit("File not found")
        return
    else:
        lol = lool.get("items")
        qw = lol[0]
        txt = f"""
<b>ɴᴀᴍᴇ :</b> <i>{qw.get("name")}</i>

<b>ғᴜʟʟ ɴᴀᴍᴇ :</b> <i>{qw.get("full_name")}</i>

<b>ʟɪɴᴋ :</b> {qw.get("html_url")}

<b>ғᴏʀᴋ ᴄᴏᴜɴᴛ :</b> <i>{qw.get("forks_count")}</i>

<b>ᴏᴘᴇɴ ɪssᴜᴇs :</b> <i>{qw.get("open_issues")}</i>

"""
        if qw.get("description"):
            txt += f'<b>ᴅᴇsᴄʀɪᴘᴛɪᴏɴ :</b> <code>{qw.get("description")}</code>'

        if qw.get("language"):
            txt += f'<b>ʟᴀɴɢᴜᴀɢᴇ :</b> <code>{qw.get("language")}</code>'

        if qw.get("size"):
            txt += f'<b>sɪᴢᴇ :</b> <code>{qw.get("size")}</code>'

        if qw.get("score"):
            txt += f'<b>sᴄᴏʀᴇ :</b> <code>{qw.get("score")}</code>'

        if qw.get("created_at"):
            txt += f'<b>ᴄʀᴇᴀᴛᴇᴅ ᴀᴛ :</b> <code>{qw.get("created_at")}</code>'

        if qw.get("archived") == True:
            txt += f"<b>ᴛʜɪs ᴘʀᴏᴊᴇᴄᴛ ɪs ᴀʀᴄʜɪᴠᴇᴅ</b>"
        await pablo.edit(txt, disable_web_page_preview=True)

<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/gbrohit/TIC-Auto-Filter-Bot-Test">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy To Heroku">
</a>
</p>
</details>

## Variables
### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
### Optional Variables
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made.Separate multiple IDs by space
* Check [info.py](https://github.com/Joelkb/DQ-The-File-Donor/blob/master/info.py) for more optional variables

## Commands
```
start - ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ
stats - ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ
logs - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ
delete - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ
users - ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ ᴏғ ᴛʜᴇ ʙᴏᴛ
chats - ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ ᴏғ ᴛʜᴇ ʙᴏᴛ
leave - ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ
disable -  ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ
ban - ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ
unban - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
channel - ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ
broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ
grp_broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs
gfilter - ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs
gfilters - ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs
delg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ
request - ᴛᴏ sᴇɴᴅ ᴀ ᴍᴏᴠɪᴇ/sᴇʀɪᴇs/ᴀɴɪᴍᴇ ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ᴀᴅᴍɪɴs. ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ
delallg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ
deletefiles - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ᴜsɪɴɢ ᴋᴇʏᴡᴏʀᴅs ꜰʀᴏᴍ ᴅᴀᴛᴀʙᴀsᴇ
batch - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs
link - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ
pbatch -  ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs, ʙᴜᴛ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ
plink - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ, ʙᴜᴛ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ
connect - ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ʙᴏᴛ
settings - ᴛᴏ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ
disconnect - ᴛᴏ ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ
connections - ᴛᴏ ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ
id - ᴛᴏ ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ
info - ᴛᴏ ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ
imdb - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴀɴʏ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ
search - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴀɴʏ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ
filter - ᴛᴏ ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
filters - ᴛᴏ ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ
del - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
delall - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ 
telegraph - ᴛᴏ ɢᴇᴛ ʟɪɴᴋ ʙʏ sᴇɴᴅɪɴɢ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ 𝟻ᴍʙ
stickerid - ᴛᴏ ɢᴇᴛ sᴛɪᴄᴋᴇʀ ɪᴅ
font - ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴛᴇxᴛ ᴛᴏ ᴅɪғғᴇʀᴇɴᴛ ғᴏɴᴛ sᴛʏʟᴇs
```

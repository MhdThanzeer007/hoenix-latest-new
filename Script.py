class script(object):
    START_TXT = """<b>𝘏𝘦𝘭𝘭𝘰𝘸 {} \n𝘔𝘺 𝘕𝘢𝘮𝘦 𝘐𝘴 <a href=https://t.me/{}>{}</a> </b>

<b>🌚 𝘏𝘦𝘺 𝘐 𝘈𝘮 𝘕𝘰𝘸 𝘐𝘯 𝘗𝘶𝘣𝘭𝘪𝘤 𝘠𝘰𝘶 𝘊𝘢𝘯 𝘜𝘴𝘦 𝘔𝘦 𝘛𝘰 𝘠𝘰𝘶𝘳 𝘎𝘳𝘰𝘶𝘱 𝘛𝘩𝘢𝘵'𝘴 𝘈𝘭𝘭 𝘔𝘢𝘯 𝘐 𝘞𝘪𝘭𝘭 𝘗𝘳𝘰𝘷𝘪𝘥𝘦 𝘔𝘰𝘷𝘪𝘦𝘴 𝘐𝘯 𝘗𝘔.

✨ 𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 :  <a href='https://t.me/mhd_thanzeer'>𝙈𝙃𝘿 𝙏𝙃𝘼𝙉𝙕𝙀𝙀𝙍</a> </b>"""
    HELP_TXT = """ᕼEY {} ℍ𝕖𝕣𝕖 𝕋𝕙𝕖 ℍ𝕖𝕝𝕡 𝔽𝕠𝕣 𝕄𝕪 ℂ𝕠𝕞𝕞𝕒𝕟𝕕𝕤 ✨️"""
    ABOUT_TXT = """<b>👨‍🔬 My Name : {}\n\n🕵‍♂ Developer : <a href='https://t.me/mhd_thanzeer'>𝙈𝙃𝘿 𝙏𝙃𝘼𝙉𝙕𝙀𝙀𝙍</a>\n\n📚 Library : 𝙿𝚁𝙾𝙶𝚁𝙰𝙼\n\n🖥 Language : 𝙿𝚈𝚃𝙷𝙾𝙽  ᴀɴᴅ  𝙲\n\n🎪 Data Base : 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱\n\n🔋 Bot Group : @wolfpackmedia </b>"""
    SOURCE_TXT = """<b>NOTE:</b>

👋<b><i>എന്താടാ മോനെ നോക്കുന്നേ നിനക്ക് ആവശ്യമായിട്ടുള്ളത് ഇവിടെ ഇല്ല 😌

</i></b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mhd_thanzeer)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>★ 𝘛𝘰𝘵𝘢𝘭 𝘍𝘪𝘭𝘦𝘴 :</b> <code>{}</code>

<b>★ 𝘛𝘰𝘵𝘢𝘭 𝘜𝘴𝘦𝘳𝘴 :</b> <code>{}</code>

<b>★ 𝘛𝘰𝘵𝘢𝘭 𝘊𝘩𝘢𝘵𝘴 :</b> <code>{}</code>

<b>★ 𝘜𝘴𝘦𝘥 𝘚𝘵𝘰𝘳𝘢𝘨𝘦 :</b> <code>{}</code>

<b>★ 𝘍𝘳𝘦𝘦 𝘚𝘵𝘰𝘳𝘢𝘨𝘦 :</b> <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

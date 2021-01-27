from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.utils import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Elite User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

userid = bot.uid

PM_IMG = "https://telegra.ph/file/70fb75f1cb3ab1500b9b4.mp4"
pm_caption = "__**MY Eʟɪᴛᴇ USERBOT IS RUNNING SUCCESSFULLY**__\n\n"

pm_caption += f" **🔱__↼MY [MASTER](tg://user?id={userid})⇀__🔱**\n\n"

pm_caption += f" **⚜️__EliteBot Version__⚜️      : __**{Eliteversion}**__**\n"

pm_caption += " **🔶__Telethon Version__🔶      : `1.15.0`**\n"

pm_caption += f" **🌐__Sudo Access__🌐          : `{sudou}`**\n"

pm_caption += f" **🔰__More Info__🔰             : [Here](https://t.me/ELiteBOT_info)**\n"

pm_caption += (
    " **❗️__Support__❗️                   : [ᴊᴏɪɴ](https://t.me/ELITES_SUPPPORT)**\n"
)

pm_caption += (
    " **🛑__Channel__🛑                   : [JOIN](https://t.me/ELITES_OFFICIAL)**\n\n"
)

pm_caption += "                ✨[REPO](https://github.com/xHOPExINFINTY/Elite_UserBot)✨  |  ✨[License](https://github.com/xHOPExINFINTY/Elite_UserBot/blob/master/LICENSE)✨"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command(
    "alive", None, "Check weather the bot is alive or not"
).add_command(
    "awake",
    None,
    "Check weather yhe bit is alive or not. In your custom Alive Pic and Alive Msg if in Heroku Vars",
).add()

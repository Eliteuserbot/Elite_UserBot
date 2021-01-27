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
pm_caption = "__**My EliteBot Is Running**__\n\n"

pm_caption += f" __↼MY MASTER⇀__\n**『[{DEFAULTUSER}](tg://user?id={userid})』**\n\n"

pm_caption += f" __EliteBot Version__ : __**{Eliteversion}**__\n"

pm_caption += f" __Sudo Access__ : `{sudou}`\n"

pm_caption += " __Telethon Version__ : `1.15.0` \n"

pm_caption += " __Support Channel__ : [ᴊᴏɪɴ](https://t.me/ELITES_SUPPORT)\n"

pm_caption += " __Creators__ : [NoBs Here](https://t.me/ELITES_OFFICIAL)\n\n"

pm_caption += "    [REPO](https://github.com/xHOPExINFINTY/Elite_UserBot) | [License](https://github.com/xHOPExINFINTY/Elite_UserBot/blob/master/LICENSE)"


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

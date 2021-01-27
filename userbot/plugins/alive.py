from userbot import *
from userbot.cmdhelp import CmdHelp
from userbot.utils import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Elite User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/c76453380cd376c960163.jpg"
pm_caption = "__**🔥🔥𝙀𝙇𝙄𝙏𝙀𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝙞𝙨 𝙊𝙣𝙡𝙞𝙣𝙚🔥🔥**__\n\n"

pm_caption += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"
)

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"Eliteẞø†     : __**{hellversion}**__\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/ELITES_SUPPORT)\n"

pm_caption += "🔥CREATOR🔥    : [NoB Here](https://t.me/BACKUP_ID_OF_A_T_1724)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/Elite-Userbot/ELITEUSERBOT) 🔹 [📜License📜](https://github.com/Elite-Userbot/ELITEUSERBOT/blob/master/LICENSE)"


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

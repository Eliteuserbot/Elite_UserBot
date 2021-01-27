### ☣️ The Most Powerfull Userbot ☣️

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f7c51539e67b483bb8d7749acca51d3a)](https://app.codacy.com/gh/Elite-Userbot/ELITEUSERBOT?utm_source=github.com&utm_medium=referral&utm_content=Elite-Userbot/ELITEUSERBOT&utm_campaign=Badge_Grade_Settings)
[![Python 3.6](https://img.shields.io/badge/Python-3.6%20or%20newer-blue.svg)](https://www.python.org/downloads/release/python-360/)
![GitHub repo size](https://img.shields.io/github/repo-size/Elite-Userbot/ELITEUSERBOT)
[![HitCount](http://hits.dwyl.com/Elite-Userbot/ELITEUSERBOT.svg)](http://hits.dwyl.com/Elite-Userbot/ELITEUSERBOT)
[![Contact Me](https://img.shields.io/badge/Telegram-Contact%20Me-informational)](https://t.me/lucifeermorningstar)


# †hê 𝙴𝙻𝙸𝚃𝙴 𝚄𝚂𝙴𝚁𝙱𝙾𝚃

This is a userbot made for telegram. I made this userbot with help of all other userbots available in telegram. All credits goes to its Respective Owners....

This is the one and only official EliteBot Userbot made by [ELITE TEAM](https://t.me/ELITES_SUPPPORT) Also join support channel and group :- https://t.me/DevilBot_Official Enjoy Your Bot!!💝
[![DevilBot logo](https://telegra.ph/file/c76453380cd376c960163.jpg)](https://t.me/A_T_1724)


### The owner would not be responsible for any kind of bans due to the bot... 

### 𝙎𝙥𝙚𝙘𝙞𝙖𝙡 𝙏𝙝𝙖𝙣𝙠𝙨 𝙩𝙤
   1. 𝙏𝙃𝙀 𝙐𝙉𝙆𝙉𝙊𝙒𝙉 𝙆𝘼𝙉𝙂𝙀𝙍 (@harshhuma) 
   2. 𝙎𝙃𝙐𝘽𝙃𝘼𝙈 (@theshubhamgundu) 
   3. 𝘿𝙀𝙑𝙄𝙇 (@lucifeermorningstar) 
  

# FORK AT YOUR OWN RISK

# Credits
### • [DevilBot](https://github.com/lucifeermorningstar/deviluserbot)
## One and only. Others with some misfuntioning brain stay out from this SUPER POWERFULL BOT😏

## Official Support
<a href="https://t.me/ELITES_SUPPPORT"><img src="https://img.shields.io/badge/Join-Support%20Channel-red.svg?style=for-the-badge&logo=Telegram"></a>
<a href="https://t.me/ELITES_SUPPPORT"><img src="https://img.shields.io/badge/Join-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>

## Video Tutorial
   𝘾𝙤𝙢𝙞𝙣𝙜 𝙎𝙤𝙤𝙣

## ⚡ Set-Up ⚡

### ✨ The Easy Way ✨

<a href="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FElite-Userbot%2FELITEUSERBOT&template=https%3A%2F%2Fgithub.com%2FElite-Userbot%2FELITEUSERBOT" rel="nofollow" style="background-color: initial; box-sizing: border-box; color: #0366d6; text-decoration-line: none;"><img alt="Deploy" data-canonical-src="https://www.herokucdn.com/deploy/button.svg" src="https://camo.githubusercontent.com/83b0e95b38892b49184e07ad572c94c8038323fb/68747470733a2f2f7777772e6865726f6b7563646e2e636f6d2f6465706c6f792f627574746f6e2e737667" style="border-style: none; box-sizing: initial; max-width: 100%;" /></a></div>

### ⚔️ The Normal Way ⚔️

Simply clone the repository and run the main file:
```sh
git clone https://github.com/Elite-Userbot/ELITEUSERBOT
cd ELITEUSERBOT
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

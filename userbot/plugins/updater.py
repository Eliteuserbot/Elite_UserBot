# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# credits to @Kraken_The_BadAss
#
# made for hellbot by team hell
"""
This module updates the userbot based on upstream revision
"""

import asyncio
import sys
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from userbot.cmdhelp import CmdHelp
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd
from var import Var

UPSTREAM_REPO_URL = Config.UPSTREAM_REPO
UPSTREAM_REPO_BRANCH = "master"
HEROKU_APP_NAME = Var.HEROKU_APP_NAME
HEROKU_API_KEY = Var.HEROKU_API_KEY
requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    ch_log = "**ChangeLog** \n\n"
    for c in repo.iter_commits(diff):
        ch_log += f"🛠️ **#{c.count()} :** [{c.summary}]({UPSTREAM_REPO_URL}/commit/{c}) 🚶 __{c.author}__\n"
    return ch_log


async def print_changelogs(event, ac_br, changelog):
    changelog_str = f"**Updates available in {ac_br} branch!\n\n{changelog}"
    if len(changelog_str) > 4096:
        await event.edit("**Changelog is too big, sending as a file.**")
        file = open("output.txt", "w+")
        file.write(changelog_str)
        file.close()
        await event.client.send_file(event.chat_id, "output.txt")
        remove("output.txt")
    else:
        await event.client.send_message(
            event.chat_id, changelog_str, link_preview=False
        )
    return True


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if HEROKU_APP_NAME is None:
            await event.edit(
                "**Please set up the** `HEROKU_APP_NAME` **variable"
                " to be able to deploy your EliteBot.**"
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await event.edit(
                f"{txt}\n" "**Invalid Heroku credentials for updating EliteBot.**"
            )
            return repo.__del__()
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except Exception as error:
            await event.edit(f"{txt}\nHere is the error log:\n`{error}`")
            return repo.__del__()
        build = app.builds(order_by="created_at", sort="desc")[0]
        if build.status == "failed":
            await event.edit("**Build failed!**\nCancelled or there were some errors.`")
            await asyncio.sleep(5)
            return await event.delete()
        else:
            await event.edit(
                "Updated your __EliteBot__ successfully sar!!!\n\nNow type .ping after 5 mins to check if I'm online"
            )
    else:
        await event.edit("**Please set up** `HEROKU_API_KEY` **variable.**")
    return


async def update(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    await event.edit(
        "Updated your __EliteBot__ successfully sar!!!\n\nNow type .ping after 5 mins to check if I'm online"
    )
    # Spin a new instance of bot
    args = [sys.executable, "-m", "userbot"]
    execle(sys.executable, *args, environ)
    return


@borg.on(admin_cmd(pattern=r"update( now| deploy|$)"))
async def upstream(event):
    "For .update command, check if the bot is up to date, update if specified"
    await event.edit("`Checking for updates, please wait...`")
    conf = event.pattern_match.group(1).strip()
    off_repo = UPSTREAM_REPO_URL
    force_update = False
    try:
        txt = "**Oops.. Updater cannot continue due to "
        txt += "some problems**\n`LOGTRACE:`\n"
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n**Directory** `{error}` **was not found.**")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n**Early failure!** `{error}`")
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"**Unfortunately, the directory {error} "
                "does not seem to be a git repository.\n"
                "But we can fix that by force updating the userbot using **"
                "`.update now.`"
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != UPSTREAM_REPO_BRANCH:
        await event.edit(
            f"**Looks like you are using your own custom branch: ({ac_br}). \n"
            "Please switch to** `master` **branch.**"
        )
        return repo.__del__()
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    """ - Special case for deploy - """
    if conf == "deploy":
        await event.edit(
            "Updated your __EliteBot__ successfully sar!!!\n\nNow type .ping after 5 mins to check if I'm online\n\n**NOTE :** Updating The Bot Wait Because huge update."
        )
        await deploy(event, repo, ups_rem, ac_br, txt)
        return

    if changelog == "" and not force_update:
        await event.edit(
            f"**Your userbot is up-to-date with `{UPSTREAM_REPO_BRANCH}`!**"
        )
        return repo.__del__()

    if conf == "" and force_update is False:
        await print_changelogs(event, ac_br, changelog)
        await event.delete()
        return await event.respond(
            "**Do** `.update now` **or** `.update deploy` **to update.**"
        )

    if force_update:
        await event.edit(
            "**Force-syncing to latest stable userbot code, please wait...**"
        )

    if conf == "now":
        await event.edit("**Perfoming a quick update, please wait...**")
        await update(event, repo, ups_rem, ac_br)
    return


CmdHelp("update").add_command(
    "update", None, "Checks if the bot is up-to-date or not"
).add_command(
    "update now", None, "Updates your bot to new codes if any else Force updates bot."
).add_command(
    "update deploy",
    None,
    "Updates your bot to new codes if any. Note that this process may take upto 30 mins",
).add()
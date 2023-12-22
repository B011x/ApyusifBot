#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ZelzalMusic import LOGGER, app, userbot
from ZelzalMusic.core.call import Zelzaly
from ZelzalMusic.misc import sudo
from ZelzalMusic.plugins import ALL_MODULES
from ZelzalMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("كود جلسة الحساب المساعد غير مدعوم ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ZelzalMusic.plugins" + all_module)
    LOGGER("ميــوزك زدثــون").info("تم تحميل الاضافات ...✓")
    await userbot.start()
    await Zelzaly.start()
    try:
        await Zelzaly.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ميــوزك زدثــون").info(
            "خطأ .. قم بفتح المكالمة في مجموعة السجل الخاصه بك\n\nجارِ ايقاف بوت الميوزك . . ."
        )
        exit()
    except:
        pass
    await Zelzaly.decorators()
    LOGGER("ميــوزك زدثــون").info(
        "\x74\x65\x6d\x20\xd8\xaa\xd9\x86\xd8\xb5\xd9\x8a\xd8\xa8\x20\xd8\xa8\xd9\x88\xd8\xaa\x20\xd9\x85\xd9\x8a\xd9\x88\xd8\xb2\xd9\x83\x20\xd8\xb2\xd8\xaf\xd8\xab\xd9\x80\xd9\x80\xd9\x88\xd9\x86\x20..\x20\xd8\xa8\xd9\x86\xd8\xac\xd8\xa7\xd8\xad\x20\xe2\x9c\x93\n\n\xd9\x84\xd8\xaa\xd8\xb5\xd9\x81\xd8\xad\x20\xd8\xa7\xd9\x88\xd8\xa7\xd9\x85\xd8\xb1\x20\xd8\xa7\xd9\x84\xd8\xa8\xd9\x88\xd8\xaa\x20\xd8\xa7\xd8\xb1\xd8\xb3\xd9\x84\x20\x28\xd8\xa7\xd9\x84\xd8\xa7\xd9\x88\xd8\xa7\xd9\x85\xd8\xb1\x29\n\xd9\x82\xd9\x86\xd8\xa7\xd8\xa9\x20\xd8\xa7\xd9\x84\xd8\xb3\xd9\x88\xd8\xb1\xd8\xb3\x20\x28\x40\x5a\x54\x68\x6f\x6e\x29"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ميــوزك زدثــون").info("جارِ ايقاف بوت الميوزك . . .")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

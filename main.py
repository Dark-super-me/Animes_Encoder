# (c) @Animes_Encoded, Dark-super-me =!
from telethon import events
from config import bot
from FastTelethonhelper import Timer, fast_upload, fast_download, Timer
import subprocess
import asyncio

loop = asyncio.get_event_loop()
@bot.on(events.NewMessage(pattern="/are_you_alive"))
async def _(event):
    await event.reply("I am alive master 😀")

@bot.on(events.NewMessage(pattern="/ls"))
async def _(event):
    p = subprocess.Popen(f'ls -lh .', stdout=subprocess.PIPE, shell=True)
    await event.reply(p.communicate()[0].decode("utf-8", "replace").strip())
   
@bot.on(events.NewMessage(pattern="/request_new_job"))
async def _(event):
    msg = await event.get_reply_message()
    r = await event.reply("Downloading..")
    file = await fast_download(bot, msg, r, "")
    await r.edit("Encoding The Video File ...")
    fcmd = f'ffmpeg -i "{file}" -preset veryfast -c:v libx265 -crf 32 -s 854x480 -map 0:v -c:a libopus -ab 32k -map 0:a -c:s copy -map 0:s? "{file}" -y'
    process = await asyncio.create_subprocess_shell(
        fcmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    await asyncio.sleep(1)
    res_file = await fast_upload(bot, f"[AG] {file}", r)
    await event.reply(file=res_file, force_document=True)
  
        
bot.start()

bot.run_until_disconnected()

    
# ran the app 









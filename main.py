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

@bot.on(events.NewMessage(pattern="/stats"))
async def _(event):
    p = subprocess.Popen(f'ls -lh .', stdout=subprocess.PIPE, shell=True)
    await event.reply(p.communicate()[0].decode("utf-8", "replace").strip())
   
@bot.on(events.NewMessage(pattern="/request_new_job"))
async def _(event):
    msg = await event.get_reply_message()
    r = await event.reply("Downloading..")
    file = await fast_download(bot, msg, r, "")
    gg = await event.client.get_entity(user.id)
    name = f"[{get_display_name(gg)}](tg://user?id={user.id})"
    await r.edit(f"Encoding The Video File for the user : {user}, check stats via /stats ...")
    subprocess.call(f'./ffmpegFDK -i "{file}" -map 0 -c:v libx265 -vf scale=854:480 -crf 32  -c:a libfdk_aac  -profile:a aac_he_v2 -vbr 2 "[AG] {file}"', shell=True)
    await asyncio.sleep(1)
    res_file = await fast_upload(bot, f"[AG] {file}", r)
    await event.reply(file=res_file, force_document=True)
  
        
bot.start()

bot.run_until_disconnected()

    
# ran the app 

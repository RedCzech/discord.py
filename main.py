import discord
from discord.ext import commands
from discord import app_commands
import random 
import json
import keep_alive
import os
import asyncio

with open('setting.json','r',encoding='utf8') as jfile:
  jdata=json.load(jfile)

bot=commands.Bot(command_prefix="%",intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(">>>Bot已就緒<<<")
  print(f"Bot : {bot.user.name}")
  print("---------------------")
  try:
    synced = await bot.tree.sync()
    print(f">>>指令同步成功: {synced} ")
  except Exception as e:
    print(f">>>指令同步失: {e} ")
  state = discord.Status.online
  game = discord.Activity(type=discord.ActivityType.streaming, name="設定", url="https://www.twitch.tv/hsiaochoco")
  await bot.change_presence(status=state, activity=game)

#bot.remove_command("help")

# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Pass | 加載 [__{extension}__]")

# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Pass | 移除加載 [__{extension}__]")

# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Pass | 重新加載 [__{extension}__]")

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(jdata['TOKEN'])

if __name__ == "__main__":
  keep_alive.keep_alive()
  asyncio.run(main())
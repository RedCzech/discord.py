import discord
from discord.ext import commands
from discord import app_commands

# 定義名為 Main 的 Cog
class Hello_Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 前綴指令
    @commands.command()
    async def Hello(self, ctx: commands.Context):
        await ctx.send(f"Hello, World!")

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "Hello":
            await message.channel.send(f"Hello, World")

    # /Hello
    @app_commands.command(name="hello",description="Say Hello")
    async def hello(self,interaction: discord.Interaction):
      await interaction.response.send_message(f"Hello {interaction.user.mention}!")

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Hello_Main(bot)) 
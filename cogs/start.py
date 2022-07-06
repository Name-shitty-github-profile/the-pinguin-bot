from nextcord.ext import commands
from nextcord import Embed
class Start(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def start(self, ctx):
    await ctx.send(embed=Embed(title="Getting started with pinguin", description="First of the pinguin language syntax is very easy, like here is how you can execute a function (the hello world)\n```\nfn dump(\"Hello, world!\")\n```\nSimple like this\nSadly the language is not published yet but soon it will be !"))

def setup(bot):
  bot.add_cog(Start(bot))

from nextcord.ext import commands
from utils import add_role
class Ready(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_ready')
  async def Ready(self):
    print('online')
    for i in self.get_guild(993737156231168151).members:
      if 993740041971048458 not in [role.id for role in i.roles] and i.bot is False:
        add_role(993737156231168151, i.id, 993740041971048458)

  @commands.Cog.listener('on_member_join')
  async def join(self, member):
    if member.bot is False:
      add_role(993737156231168151, member.id, 993740041971048458)
    else:
      add_role(993737156231168151, member.id, 993740207025311834)

def setup(bot):
  bot.add_cog(Ready(bot))

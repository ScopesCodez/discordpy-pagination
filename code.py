# First, we need to import the packages we need.
import discord
from discord.ext import commands
from discord.ext.buttons import Paginator

# Then, we create our bot instance.
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

# This is an example list which will have some names.
some_names = ["Seif", "Wessam", "Scopes"]

# Now we will make the paginator class.
class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass
          
# Now let's make a command that sends our list of names as pages!
@bot.command()
async def names(ctx):
  pager = Pag(timeout=60, entries=some_names, length=1, prefix="", suffix="")
  # pager is our Paginator instance.
  # timeout attr is how many time (in seconds) for the reactions to disappear.
  # entries attr is the list you want to paginate.
  # length attr is how many items from that list in a single page.
  # prefix attr is what's above each item in the page.
  # suffix attr is what's below each item in the page.
  await pager.start(ctx)
  
bot.run("your bot's token")

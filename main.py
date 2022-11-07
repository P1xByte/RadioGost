from discord import FFmpegPCMAudio, Activity, ActivityType
from discord.ext.commands import Bot
import keep_alive
bot = Bot(command_prefix="-", help_command=None)

@bot.event
async def on_ready() -> None:
    print(f"{bot.user} ин да хаус!.")
    await bot.change_presence(activity=Activity(name="музыку",  type=ActivityType.listening))

    voice_channel = bot.get_channel(884421383940087808)
    player = await voice_channel.connect()
    player.play(FFmpegPCMAudio("http://89.185.94.89:8000/rd_72_01"))
    
keep_alive.keep_alive()
bot.run("MTAzODkwNzg3MTA3ODkyODQ1Ng.GVZw0T.5V0LdQgBZL0g9jo_LHhh17FVa7Mp92SnY1Rias")

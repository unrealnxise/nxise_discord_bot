import discord
from discord.ext import commands
from config import settings
from forms import Forms
import time

bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())
bot.remove_command('help')

f = Forms()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('$help'))

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(910448872919302154)
    start_role = discord.utils.get(member.guild.roles, id=921399652010590238)

    await member.add_roles(start_role)
    await channel.send(embed=f.join(bot, member))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send('🙇 У вас недостаточно прав')
    else:
        await ctx.send('😥 Непонимаю')

@bot.command()
async def help(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send(embed = f.help(bot))

@bot.command()
async def hug(ctx, member : discord.Member):
    await ctx.channel.purge(limit=1)
    author = ctx.author

    await ctx.send(embed=f.hug(bot, author, member))

# Команды для администрации
@bot.command()
@commands.has_any_role('💀 Жнец')
async def clear(ctx, amount=500 ):
    author = ctx.message.author
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(embed=f.clear(bot, author))

    time.sleep(2)
    await ctx.channel.purge(limit=1)

@bot.command()
@commands.has_any_role('💀 Жнец')
async def kick(ctx, member : discord.Member, reason=None):
    author = ctx.message.author
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    await ctx.send(embed=f.kick(bot, member, author, reason))

bot.run(settings['token'])

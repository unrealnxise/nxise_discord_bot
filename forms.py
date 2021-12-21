import discord
from discord.ext import commands
from config import settings
import random as r

hugs_gifs = ['https://media.giphy.com/media/u9BxQbM5bxvwY/giphy.gif',
             'https://media.giphy.com/media/1434tCcpb5B7EI/giphy.gif',
             'https://media.giphy.com/media/sUIZWMnfd4Mb6/giphy.gif',
             'https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif',
             'https://media.giphy.com/media/DjczAlIcyK1Co/giphy.gif']

class Forms():
    def help(self, bot):
        emb = discord.Embed(title='Основное', colour=discord.Colour.green(),
                            description='Команды для работы с ботом')
        emb.set_thumbnail(url='https://www.freeiconspng.com/uploads/helping-hand-icon-png-10.png')
        emb.add_field(name='$hug _<@user>_', value='обнимает отмеченного вами пользователя')
        emb.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

        return emb

    def clear(self, bot, author):
        emb = discord.Embed(title='Чат был очищен', colour=discord.Colour.blue())
        emb.set_thumbnail(url='https://www.freeiconspng.com/uploads/clear-icon-25.png')
        emb.set_footer(text=author.name, icon_url=author.avatar_url)

        return emb

    def kick(self, bot, member, author, text):
        emb = discord.Embed(title='Был выгнан с сервера!', description=f'{member.display_name}')
        emb.add_field(name='Причина:', value=f'{text}')
        emb.set_thumbnail(url='https://www.freeiconspng.com/uploads/kickboxing-icon-9.png')
        emb.set_footer(text=author.name, icon_url=author.avatar_url)

        return emb

    def join(self, bot, member):
        emb = discord.Embed(title=f'Добро пожаловать, **{member}** на наш сервер!', colour=discord.Colour.gold())
        emb.set_image(url=member.avatar_url)

        return emb

    def hug(self, bot, author, member):
        if author == member:
            emb = discord.Embed(description=f'**{author.name}** не возможно обнять самого себя',
                                colour=discord.Colour.green())
        else:
            emb = discord.Embed(description=f'**{author.name}** обнял **{member.display_name}**',
                                colour=discord.Colour.green())
            emb.set_image(url=r.choice(hugs_gifs))

        return emb

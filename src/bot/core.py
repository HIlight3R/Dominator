import discord
from discord.ext import commands

from config import PREFIX, TOKEN, DELETE_COMMANDS, MUTE_ROLE_NAME

# Настройка префикса для команд
client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')


def main():
    @client.event
    async def on_ready():
        """Сообщение при подключении"""
        print('Бот запущен')

    @client.command(name="ping")
    async def _ping(ctx):
        """Проверить работоспособность"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        author = ctx.message.author
        await ctx.send(f'{author.mention} Pong!')

    @client.command(name="help")
    async def _help(ctx):
        """Справка по командам"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        embed = discord.Embed(title='Справка по командам',
                              description=f'Все команды у этого бота начинаются с префикса "{PREFIX}" (без кавычек).',
                              color=discord.Color.orange())
        embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        embed.add_field(name=f'{PREFIX}help', value='Выводит эту справку.')
        embed.add_field(name=f'{PREFIX}ping', value='Проверяет работоспособность бота.')
        embed.add_field(name=f'{PREFIX}clear [КОЛИЧЕСТВО]',
                        value='Очищает в чате последние КОЛИЧЕСТВО сообщений. По умолчанию очищает весь чат.')
        embed.add_field(name=f'{PREFIX}kick ПОЛЬЗОВАТЕЛЬ [ПРИЧИНА]',
                        value='Выгоняет участника ПОЛЬЗОВАТЕЛЬ из сервера по причине ПРИЧИНА. По умолчанию без '
                              'причины.')
        embed.add_field(name=f'{PREFIX}ban ПОЛЬЗОВАТЕЛЬ [ПРИЧИНА]',
                        value='Навсегда блокирует участника ПОЛЬЗОВАТЕЛЬ на сервере по причине ПРИЧИНА. По умолчанию '
                              'без причины.')
        embed.add_field(name=f'{PREFIX}unban ID_ПОЛЬЗОВАТЕЛЯ',
                        value='Разблокирует участника с ID ID_ПОЛЬЗОВАТЕЛЯ на сервере, если он был заблокирован.')
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @client.command(name='clear')
    @commands.has_permissions(administrator=True)
    async def _clear(ctx, amount=None):
        """Очистка чата"""
        if amount:
            await ctx.channel.purge(limit=amount + 1)
        else:
            await ctx.channel.purge()

    @client.command(name='kick')
    @commands.has_permissions(administrator=True)
    async def _kick(ctx, member: discord.Member, *, reason: str = None):
        """Выгнать участника"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        await member.kick(reason=reason)
        if reason:
            await ctx.send(f'Участник {member.mention} выгнан с сервера.\nПричина: "{reason}".')
        else:
            await ctx.send(f'Участник {member.mention} выгнан с сервера без причины.')

    @client.command(name='ban')
    @commands.has_permissions(administrator=True)
    async def _ban(ctx, member: discord.Member, *, reason: str = None):
        """Выгнать и заблокировать участника"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        await member.ban(reason=reason)
        if reason:
            await ctx.send(f'Участник {member.mention} забанен на сервере.\nПричина: "{reason}".')
        else:
            await ctx.send(f'Участник {member.mention} забанен на сервере без причины.')

    @client.command(name='unban')
    @commands.has_permissions(administrator=True)
    async def _unban(ctx, *, user_id: int):
        """Разблокировать участника"""
        await ctx.message.delete()
        try:
            user = await client.fetch_user(user_id=user_id)
            await ctx.guild.unban(user)
            await ctx.send(f'Участник с ID {user_id} успешно разбанен.')
        except:
            await ctx.send(f'Участник с ID {user_id} не забанен, поэтому не может быть разбанен.')

    @client.command(name='mute')
    @commands.has_permissions(administrator=True)
    async def _mute(ctx, member: discord.Member):
        """Запретить писать участнику в чат"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        mute_role = discord.utils.get(ctx.message.guild.roles, name=MUTE_ROLE_NAME)
        await member.add_roles(mute_role)
        await ctx.send(f'Участник {member.mention} теперь может только читать сообщения.')

    @client.command(name='unmute')
    @commands.has_permissions(administrator=True)
    async def _unmute(ctx, member: discord.Member):
        """Разрешить писать участнику в чат"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        mute_role = discord.utils.get(ctx.message.guild.roles, name=MUTE_ROLE_NAME)
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            await ctx.send(f'Участник {member.mention} снова может писать в чат.')
        else:
            await ctx.send(f'Участник {member.mention} не в муте, поэтому не может быть размучен.')

    # Запуск бота
    client.run(TOKEN)
    print('Бот остановлен')

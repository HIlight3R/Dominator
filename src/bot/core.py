import discord
from discord.ext import commands

from config import PREFIX, TOKEN, DELETE_COMMANDS, MUTE_ROLE_ID, USE_AUTO_ROLE, AUTO_ROLE_ID, USE_NEWCOMER_NOTICE, \
    NEWCOMER_NOTICE_CHANNEL, SEND_PUNISHMENT_PERSONAL_MESSAGE, USE_CHAT_FILTRATION, BAD_WORD_LIST

# Настройка префикса для команд
client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')


def main():
    @client.event
    async def on_connect():
        """Сообщение при подключении"""
        print('Бот подключен')
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{PREFIX}help'))

    @client.event
    async def on_member_join(member: discord.Member):
        if USE_AUTO_ROLE or USE_NEWCOMER_NOTICE:
            if USE_AUTO_ROLE:
                role = discord.utils.get(member.guild.roles, id=AUTO_ROLE_ID)
                await member.add_roles(role)
            if USE_NEWCOMER_NOTICE:
                channel = client.get_channel(NEWCOMER_NOTICE_CHANNEL)
                await channel.send(
                    embed=discord.Embed(description=f'Пользователь {member.mention} присоединился к серверу.',
                                        color=0xff8000))

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(
                f'{ctx.author.mention}, такой команды не существует, воспользуйтесь справкой, введя {PREFIX}help.')

    @client.event
    async def on_message(message: discord.Message):
        if USE_CHAT_FILTRATION:
            await client.process_commands(message)
            msg = message.content.lower()
            if msg in BAD_WORD_LIST:
                await message.delete()
                await message.channel.send(f'{message.author.mention}, не надо так писать!')

    @client.event
    async def on_resumed():
        """Сообщение при повторном подключении"""
        print('Бот снова подключен')

    @client.event
    async def on_disconnect():
        """Сообщение при отключении"""
        print('Бот отключен')

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
        embed.add_field(name=f'{PREFIX}mute ПОЛЬЗОВАТЕЛЬ',
                        value='Навсегда запрещает участнику ПОЛЬЗОВАТЕЛЬ писать сообщения в текстовых каналах.')
        embed.add_field(name=f'{PREFIX}unmute ПОЛЬЗОВАТЕЛЬ',
                        value='Разрешает участнику ПОЛЬЗОВАТЕЛЬ писать сообщения в текстовые каналы, если до этого он '
                              'не мог это делать.')
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @client.command(name='clear')
    @commands.has_permissions(administrator=True)
    async def _clear(ctx, amount=None):
        """Очистка чата"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        if amount:
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.channel.purge()

    @client.command(name='kick')
    @commands.has_permissions(administrator=True)
    async def _kick(ctx, member: discord.Member, *, reason: str = None):
        """Кикнуть участника"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        await member.kick(reason=reason)
        if reason:
            await ctx.send(f'Участник {member.mention} выгнан с сервера.\nПричина: "{reason}".')
            if SEND_PUNISHMENT_PERSONAL_MESSAGE:
                await member.send(f'Вы были выгнаны с сервера по причине: "{reason}".')
        else:
            await ctx.send(f'Участник {member.mention} выгнан с сервера без причины.')
            if SEND_PUNISHMENT_PERSONAL_MESSAGE:
                await member.send('Вы были выгнаны с сервера без причины.')

    @client.command(name='ban')
    @commands.has_permissions(administrator=True)
    async def _ban(ctx, member: discord.Member, *, reason: str = None):
        """Забанить участника"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        await member.ban(reason=reason)
        if reason:
            await ctx.send(f'Участник {member.mention} забанен на сервере.\nПричина: "{reason}".')
            if SEND_PUNISHMENT_PERSONAL_MESSAGE:
                await member.send(f'Вы были забанены на сервере по причине: "{reason}".')
        else:
            await ctx.send(f'Участник {member.mention} забанен на сервере без причины.')
            if SEND_PUNISHMENT_PERSONAL_MESSAGE:
                await member.send('Вы были забанены на сервере без причины.')

    @client.command(name='unban')
    @commands.has_permissions(administrator=True)
    async def _unban(ctx, *, user_id: int):
        """Разбанить участника"""
        await ctx.message.delete()
        try:
            user = await client.fetch_user(user_id=user_id)
            await ctx.guild.unban(user)
            await ctx.send(f'Участник с ID {user_id} успешно разбанен.')
            if SEND_PUNISHMENT_PERSONAL_MESSAGE:
                await user.send('Вы были разбанены на сервере.')
        except discord.DiscordException:
            await ctx.send(f'Участник с ID {user_id} не забанен, поэтому не может быть разбанен.')

    @client.command(name='mute')
    @commands.has_permissions(administrator=True)
    async def _mute(ctx, member: discord.Member):
        """Замьютить участника"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        mute_role = discord.utils.get(ctx.message.guild.roles, id=MUTE_ROLE_ID)
        await member.add_roles(mute_role)
        await ctx.send(f'Участник {member.mention} теперь может только читать сообщения.')
        if SEND_PUNISHMENT_PERSONAL_MESSAGE:
            await member.send('Вы были замьючены на сервере.')

    @client.command(name='unmute')
    @commands.has_permissions(administrator=True)
    async def _unmute(ctx, member: discord.Member):
        """Размьютить участника"""
        if DELETE_COMMANDS:
            await ctx.message.delete()
        mute_role = discord.utils.get(ctx.message.guild.roles, id=MUTE_ROLE_ID)
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            await ctx.send(f'Участник {member.mention} снова может писать в чат.')
            if SEND_PUNISHMENT_PERSONAL_MESSAGE:
                await member.send('Вы были размьючены на сервере.')
        else:
            await ctx.send(f'Участник {member.mention} не в мьюте, поэтому не может быть размьючен.')

    @_kick.error
    @_ban.error
    @_unban.error
    @_mute.error
    @_unmute.error
    async def moderation_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f'{ctx.author.mention}, вы неверно ввели аргументы, воспользуйтесь командой {PREFIX}help для справки.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{ctx.author.mention}, у вас недостаточно прав для выполнения данной команды.')

    # Запуск бота
    client.run(TOKEN)

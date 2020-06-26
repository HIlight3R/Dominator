import logging
import sys

from discord.ext import commands

import config

# Получение аргумента командной строки, отвечающего за уровень логирования
try:
    argument = sys.argv[1]
except IndexError:
    argument = '-i'

# Задаем соответствующие параметры логирования
logFormat = '%(asctime)s — %(levelname)s — %(message)s'
if argument == '-d':
    logLevel = logging.DEBUG
    del logFormat
    logFormat = '%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s'
elif argument == '-i':
    logLevel = logging.INFO
elif argument == '-w':
    logLevel = logging.WARNING
elif argument == '-e':
    logLevel = logging.ERROR
elif argument == '-c':
    logLevel = logging.CRITICAL
else:
    logLevel = config.LOG_MODE_DEFAULT

if config.LOG_IN_FILE:
    logging.basicConfig(level=logLevel, format=logFormat, filename=config.LOG_FILE_NAME, filemode=config.LOG_MODE)
else:
    logging.basicConfig(level=logLevel, format=logFormat)

# Настройка префикса для команд
client = commands.Bot(command_prefix=config.PREFIX)
logging.debug('Префикс успешно задан.')


@client.event
async def on_ready():
    logging.info('Бот успешно запущен.')


@client.command(pass_content=True)
async def hello(ctx, arg=None):
    author = ctx.message.author
    if arg is None:
        await ctx.send(
            f'Здравствуйте, {author.mention}! Вы ничего не напечатали. После команды {config.PREFIX}hello Вы должны '
            f'напечатать что-нибудь.')
    else:
        await ctx.send(f'Привет, {author.mention}! Ты напечатал(а): "{arg}", круто.')


# Запуск бота
client.run(config.TOKEN)
logging.info('Программа завершила свою работу.')

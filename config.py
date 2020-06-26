import logging

# ----------
# Основное
# ----------


# Токен бота, можно получить в https://discord.com/developers.
TOKEN = 'TOKEN'

# Префикс для команд.
PREFIX = '$'

# Записывать события в файл лога? В случае False лог будет выводиться в консоль.
LOG_IN_FILE = False

# Имя файла лога вместе с расширением файла.
LOG_FILE_NAME = 'global.log'

# Способ логирования ('a' - запись в конец файла, 'w' - полная перезапись файла при каждом запуске.
LOG_MODE = 'a'

# Уровень логирования по умолчанию (если не дано аргументов): logging. + DEBUG, INFO, WARNING, ERROR или CRITICAL.
LOG_MODE_DEFAULT = logging.INFO

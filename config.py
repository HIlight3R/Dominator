# --------
# Основное
# --------

# Токен бота, можно получить в https://discord.com/developers.
TOKEN = 'TOKEN'

# Префикс для команд. У каждого бота на сервере должен быть различным.
PREFIX = '$'

# Удаляет сообщение с командой перед выводом ответа?
DELETE_COMMANDS = True

# ---------
# Модерация
# ---------

# ID роли, которая будет выдаваться участнику при муте. Для корректной работы роль не должна иметь права
# "Отправлять сообщения" и "Отправлять TTS сообщения".
MUTE_ROLE_ID = 12345678123456789

# Отправлять личные сообщения участникам при наказаниях и их отмене.
SEND_PUNISHMENT_PERSONAL_MESSAGE = True

# --------
# Автороль
# --------

# Использовать автороль?
USE_AUTO_ROLE = True

# ID роли для выдачи.
AUTO_ROLE_ID = 123456789123456789

# ---------------
# Новые участники
# ---------------

# Уведомлять в чат о новом участнике?
USE_NEWCOMER_NOTICE = True

# ID канала для получения сообщения, что участник присоединился к серверу.
NEWCOMER_NOTICE_CHANNEL = 123456789123456789

# ---------------
# Фильтрация чата
# ---------------

# Использовать фильтрацию чата?
USE_CHAT_FILTRATION = True

# Список плохих слов в нижнем регистре.
BAD_WORD_LIST = ('some_word', 'bad_word', 'the_worst_word')

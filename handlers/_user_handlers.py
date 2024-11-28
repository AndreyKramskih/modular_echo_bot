# Из  aiogram.types импортируем класс Message
from aiogram.types import Message
# Из aiogram.filters импортируем класс Command, чтобы фильтровать
# апдейты по наличию в них команд, то есть сочетаний символов, начинающихся со знака "/".
from aiogram.filters import Command, CommandStart
# Сообщения для отправки пользователям будем брать из словаря LEXICON_RU
# по соответствующим ключам '/start' для хэндлера process_start_command и '/help'
# для хэндлера process_help_command. Для этого нужно импортировать
# словарь из соответствующего модуля соответствующего пакета:
from lexicon._llexicon import LEXICON_RU

# Этот хэндлер срабатывает на команду /start
@dp.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'])

# Этот хэндлер срабатывает на команду /help
@dp.message(Command())
async def process_help_command(message:Message):
    await message.answer(text=LEXICON_RU['/help'])

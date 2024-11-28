# появился импорт класса Router
from aiogram import Router

# Инициализируем роутер уровня модуля
router=Router()

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
@router.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'])

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message:Message):
    await message.answer(text=LEXICON_RU['/help'])

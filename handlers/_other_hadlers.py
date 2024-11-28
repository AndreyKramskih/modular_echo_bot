# появился импорт класса Router
from aiogram import Router

# Инициализируем роутер уровня модуля
router = Router()

from aiogram.types import Message
from lexicon._llexicon import LEXICON_RU

# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message:Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
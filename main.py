# Импортируем библиотеку asyncio, чтобы иметь возможность добавить асинхронную функцию main в цикл событий.
import asyncio

#Импортируем классы бота и диспетчера
from aiogram import Bot, Dispatcher

#Из модуля конфигурации config.py пакета config_data импортируем класс Config и функцию load_config,
# чтобы сконфигурировать бота, используя данные из файла .env.
from config_data._config import Config, load_config

# импортировать модули с хэндлерами
from handlers import _other_hadlers, _user_handlers

# Функция конфигурирования и запуска бота
async def main()->None:
    config:Config=load_config(None)

    # Инициализируем бот и диспетчер
    bot=Bot(token=config.tg_bot.token)
    dp=Dispatcher()
    print(config.tg_bot.token)
    # Регистриуем роутеры в диспетчере
    dp.include_router(_user_handlers.router)
    dp.include_router(_other_hadlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Т.к. функция main асинхронная, мы не можем ее просто вызвать, как привыкли это делать
# с синхронными функциями, но зато мы можем запустить цикл событий и добавить функцию в него.

asyncio.run(main())





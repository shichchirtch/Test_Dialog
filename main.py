import asyncio
from command_handlers import ch_router
# from aiogram import Dispatcher
# from callback_handlers import cb_router
from bot_instans import bot, bot_storage_key, dp
from aiogram_dialog import setup_dialogs
from dialogs import (start_dialog, second_dialog, drei_dialog,
                     vier_dialog, checkbox_dialog, six_dialog,
                     radio_dialog, picture_dialod, dinamic_media_dialod,
                     text_input_dialog, every_content_dialog)
from start_menu import set_main_menu_2



async def main():


    # dp = Dispatcher(storage=aio_storage)
    dp.startup.register(set_main_menu_2)
    await dp.storage.set_data(key=bot_storage_key, data={})

    dp.include_router(ch_router)
    dp.include_router(start_dialog)
    dp.include_router(second_dialog)
    dp.include_router(drei_dialog)
    dp.include_router(vier_dialog)
    dp.include_router(checkbox_dialog)
    dp.include_router(six_dialog)
    dp.include_router(radio_dialog)
    dp.include_router(picture_dialod)
    dp.include_router(dinamic_media_dialod)
    dp.include_router(text_input_dialog)
    dp.include_router(every_content_dialog)
    # scheduler.start()
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    setup_dialogs(dp)
    await dp.start_polling(bot)


asyncio.run(main())


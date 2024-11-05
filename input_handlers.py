import asyncio
from aiogram.types import Message
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from aiogram_dialog import DialogManager, ShowMode


# Хэндлер, который сработает, если пользователь ввел корректный возраст
async def correct_age_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    await message.answer(text=f'Вам {text}')
    await asyncio.sleep(1)
    await dialog_manager.next()


# Хэндлер, который сработает на ввод некорректного возраста
async def error_age_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError):
    await message.answer(text='Вы ввели некорректный возраст. Попробуйте еще раз')
    await asyncio.sleep(1)




# Хэндлер, который сработает, если пользователь ввел корректный возраст
async def correct_name_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    await message.answer(text=f'Привет {text}')
    await asyncio.sleep(1)
    await dialog_manager.next()


# Хэндлер, который сработает на любой апдейт типа `Message`
# за исключением команды /start
async def message_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager) -> None:
    dialog_manager.show_mode = ShowMode.NO_UPDATE
    await message.send_copy(message.chat.id)

async def message_content_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager) -> None:
    dialog_manager.show_mode = ShowMode.NO_UPDATE
    await message.answer('Gut genacht !')





from aiogram.types import User, ContentType
from aiogram_dialog import DialogManager
from aiogram.fsm.context import FSMContext
from bot_base import users_db
from aiogram_dialog.api.entities import MediaAttachment, MediaId

# Хэндлер для диалога

async def get_name(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    if dialog_manager.start_data:
        getter_data = {'username': event_from_user.username or 'Stranger',
                   'first_show': True}
        dialog_manager.start_data.clear()

    else:
        getter_data = {'first_show': False}
    return getter_data

async def get_categories(**kwargs):
    categories = [
        ('Техника', 1),
        ('Одежда', 2),
        ('Обувь', 3),
    ]
    return {'categories': categories}


async def five_getter(dialog_manager: DialogManager, **kwargs):
    checked = dialog_manager.dialog_data.get('is_checked')
    return {'checked': checked,
            'not_checked': not checked}



async def get_topics_for_sex_dialogs(dialog_manager: DialogManager,
                                     event_from_user: User,
                                     state:FSMContext, **kwargs):
    topics = [
        ("IT", '1'),
        ("Дизайн", '2'),
        ("Наука", '3'),
        ("Общество", '4'),
        ("Культура", '5'),
        ("Искусство", '6'),
    ]
    us_basa = users_db[event_from_user.id]  # Получаю по ключу tg_id доступ к БД Юзера
    us_dict = await state.get_data()   #  Получаю словарь юзера в сторадж
    getters_dict = {"topics": topics, 'us_dict':us_dict, 'us_basa':us_basa}
    return getters_dict


async def get_languages(dialog_manager: DialogManager, **kwargs):
    # checked2 = dialog_manager.find('radio_lang')
    # print('checked2 = ', checked2)   #   checked2 =  <aiogram_dialog.widgets.kbd.select.ManagedRadio object at 0x000001EC815D68D0>
    checked = dialog_manager.find('radio_lang').get_checked()  # Возвращает ключ в словаре language

    language = {
        '1': 'en',
        '2': 'ru',
        '3': 'fr'
    }
    chosen_lang = language['2' if not checked else checked]
    lang = {
        'ru': {
            '1': '🇬🇧 Английский',
            '2': '🇷🇺 Русский',
            '3': '🇫🇷 Французский',
            'text': 'Выберите язык'
        },
        'en': {
            '1': '🇬🇧 English',
            '2': '🇷🇺 Russian',
            '3': '🇫🇷 French',
            'text': 'Choose language'
        },
        'fr': {
            '1': '🇬🇧 Anglais',
            '2': '🇷🇺 Russe',
            '3': '🇫🇷 Français',
            'text': 'Choisissez la langue'
        }
    }
    languages = [
        (f"{lang[chosen_lang]['1']}", '1'),
        (f"{lang[chosen_lang]['2']}", '2'),
        (f"{lang[chosen_lang]['3']}", '3'),
    ]
    return {"languages": languages,
            'text': lang[chosen_lang]['text']}




async def get_foto(**kwargs):
    image_id = "AgACAgIAAxkBAAIuVmcmtjHVR275ygerwj5p0uNVSd8GAAKp5DEbuIc5SXXnu3kXOw1wAQADAgADeAADNgQ"  # Your file_id
    image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_id))
    text_data = 'my text'
    return {'photo': image, 'text':text_data}







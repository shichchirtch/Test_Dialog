from aiogram_dialog import Dialog, DialogManager, StartMode, Window, ShowMode
from getters import (get_name, get_categories, five_getter,
                     get_topics_for_sex_dialogs, get_languages, get_foto)
from bot_instans import (FSM_ST, FSM_ST2, FSM_ST3, FSM_ST4, FSM_ST5, FSM_ST6,
                         FSM_ST7, FSM_ST_foto, FSM_ST_foto_dinamic, FSM_ST8, FSM_ST9)
from aiogram_dialog.widgets.text import Const, Format, List, Multi
from aiogram_dialog.widgets.kbd import (Url, Button, Row, Group, Column, Select,
                                        Checkbox, Multiselect, Radio)
from aiogram_dialog.widgets.input import TextInput, ManagedTextInput, MessageInput
from aiogram_dialog.widgets.media import StaticMedia, DynamicMedia
from aiogram.types import User, ContentType
from callback_dialogs import (yes_click_process,
                              no_click_process, button_clicked,
                              category_selection, checkbox_clicked,
                              category_filled,
                              button_in_six_clicked, radio_button_clicked, go_second,
                              go_first, go_third, go_fourth, go_next, go_back, button_clicked_to_five )
import operator
from dialog_functions import age_check, name_check
from input_handlers import (error_age_handler, correct_age_handler,
                            correct_name_handler, message_handler, message_content_handler)
from filters import TEXT_FILTER



start_dialog = Dialog(
    Window(
        Format('<b>Привет, {username}!</b>\n', when='first_show'),
        Const('Это <b>первое</b> окно диалога. Выбери в какое окно хочешь перейти 👇'),
        Row(
            Button(Const('2'), id='b_second', on_click=go_second),
            Button(Const('3'), id='b_third', on_click=go_third),
            Button(Const('4'), id='b_fourth', on_click=go_fourth),
        ),
        Button(Const('Вперед ▶️'), id='b_next', on_click=go_next),
        getter=get_name,
        state=FSM_ST.start
    ),
    Window(
        Const('Это <b>второе</b> окно диалога. Выбери в какое окно хочешь перейти 👇'),
        Row(
            Button(Const('1'), id='b_first', on_click=go_first),
            Button(Const('3'), id='b_third', on_click=go_third),
            Button(Const('4'), id='b_fourth', on_click=go_fourth),
        ),
        Row(
            Button(Const('◀️ Назад'), id='b_back', on_click=go_back),
            Button(Const('Вперед ▶️'), id='b_next', on_click=go_next),
        ),
        state=FSM_ST.window_2
    ),
    Window(
        Const('Это <b>третье</b> окно диалога. Выбери в какое окно хочешь перейти 👇'),
        Row(
            Button(Const('1'), id='b_first', on_click=go_first),
            Button(Const('2'), id='b_second', on_click=go_second),
            Button(Const('4'), id='b_fourth', on_click=go_fourth),
        ),
        Row(
            Button(Const('◀️ Назад'), id='b_back', on_click=go_back),
            Button(Const('Вперед ▶️'), id='b_next', on_click=go_next),
        ),
        state=FSM_ST.window_3
    ),
    Window(
        Const('Это <b>четвертое</b> окно диалога. Выбери в какое окно хочешь перейти 👇'),
        Row(
            Button(Const('1'), id='b_first', on_click=go_first),
            Button(Const('2'), id='b_second', on_click=go_second),
            Button(Const('3'), id='b_third', on_click=go_third),
        ),
        Button(Const('◀️ Назад'), id='b_back', on_click=go_back),
        state=FSM_ST.window_4
    ),
)



second_dialog = Dialog(
    Window(
        Const('Это сообщение с инлайн-кнопкой. На кнопку можно нажать, '
              'и осуществить переход по какой-то ссылке'),
        Url(text=Const('Перейти'),
            url=Const('https://t.me/divdiv2'),
            id='url_button'),
        state=FSM_ST2.lernen,
    ),
)

drei_dialog = Dialog(
    Window(
        Const('<b>ВЫ ПОПАЛИ В ДИАЛОГ DREI</b>\n\nНа кнопки из этого сообщения можно нажать!'),
        Group(Row(Button(text=Const('Нажми!'),  id='button_1', on_click=button_clicked),
                     Button(text=Const('И меня!'), id='button_2', on_click=button_clicked),
                     Button(text=Const('А меня не надо !'), id='button_3', on_click=button_clicked)),
            Row(Button(
                    text=Const('Нажми!'),
                    id='button_1',
                    on_click=button_clicked),
                Button(
                    text=Const('И меня!'),
                    id='button_2',
                    on_click=button_clicked),),
                Row(Button(
                    text=Const('И меня тоже!'),
                    id='button_3',
                    on_click=button_clicked)),
        ),
        state=FSM_ST3.drei
    ),
    Window (
        Const('Вы во втором окне диалога drei'),
        Button(
                    text=Const('go to five'),
                    id='button_to_five',
                    on_click=button_clicked_to_five),
        state=FSM_ST3.drei_two)
)

vier_dialog = Dialog(
    Window(
        Const(text='ВЫ ВНУТРИ ДИАЛОГА VIER 🔥\n\nВыберите категорию:'),
        Group(
            Select(
                Format('{item[0]}'),
                id='categ',
                item_id_getter=lambda x : f'{x[0]} {x[1]}',
                items='categories',
                on_click=category_selection,
            ),
            width=2
        ),
        state=FSM_ST4.vier,
        getter=get_categories
    ),
)



checkbox_dialog = Dialog(
    Window(
        Const(text='Демонстрация работы виджета <code>Checkbox</code>\n'),
        Const(text='Сейчас дополнительного текста нет', when='not_checked'),
        Const(text='Дополнительный текст есть:\n<b>Это дополнительный текст</b>', when='checked'),
        Checkbox(
            checked_text=Const('🔘 Отключить'),
            unchecked_text=Const('⚪️ Включить'),
            id='checkbox',
            default=False,
            on_state_changed=checkbox_clicked,
        ),
        state=FSM_ST5.five,
        getter=five_getter
    ),
)


six_dialog = Dialog(
    Window(
        Const(text='Отметьте темы новостей 👇'),
        Column(
            Multiselect(
                checked_text=Format('🔘 {item[0]}'),
                unchecked_text=Format('⚪️ {item[0]}'),
                id='multi_topics',
                item_id_getter=lambda x : f'{x[0]} {x[1]}',
                items="topics",
                min_selected=2,
                max_selected=4,
                on_state_changed=category_filled
            ),
            Button (text=Const('Подтвердите выбор'),
                    id='confirm_choice',
                    on_click=button_in_six_clicked)
        ),
        state=FSM_ST6.sex,
        getter=get_topics_for_sex_dialogs
    ),
)


radio_dialog = Dialog(
    Window(
        Format(text='{text}'),
        Column(
            Radio(
                checked_text=Format('🔘 {item[0]}'),
                unchecked_text=Format('⚪️ {item[0]}'),
                id='radio_lang',
                item_id_getter=operator.itemgetter(1),
                items="languages",
                on_state_changed=radio_button_clicked
            ),
        ),
        state=FSM_ST7.radio,
        getter=get_languages
    ),
)


picture_dialod =  Dialog(
    Window(
        Const(text='Даже кот умеет программировать!'),
        StaticMedia(
            # path='https://i.postimg.cc/N0qZqtYn/2024-10-25-170954356.png',
            url='https://i.postimg.cc/N0qZqtYn/2024-10-25-170954356.png',
            type=ContentType.PHOTO
        ),
        state=FSM_ST_foto.send_foto,
    ),
)

dinamic_media_dialod =  Dialog(
    Window(
        Format(text='{text}'),
        DynamicMedia("photo"),
        state=FSM_ST_foto_dinamic.foto_dinamic,
        getter=get_foto,
    ),
)


text_input_dialog = Dialog(
    Window(
        Const(text='Введите ваш возраст'),
        TextInput(
            id='age_input',
            type_factory=age_check,
            on_success=correct_age_handler,
            on_error=error_age_handler,
        ),
        state=FSM_ST8.input_text,
    ),
    Window(
        Const(text='Введите ваше Имя'),
        TextInput(
            id='name_input',
            type_factory=name_check,
            on_success=correct_name_handler,
            on_error=error_age_handler,
        ),
        state=FSM_ST8.get_name,
    ),
)

every_content_dialog = Dialog(
    Window(
        Const(text='Пришлите мне что-нибудь и я отправлю вам копию обратно'),
        MessageInput(
            func=message_handler,
            content_types=ContentType.ANY,
            filter=TEXT_FILTER()
        ),
        MessageInput(
            func=message_content_handler,
            content_types=ContentType.ANY,
        ),
        state=FSM_ST9.any_content,
    ),
)





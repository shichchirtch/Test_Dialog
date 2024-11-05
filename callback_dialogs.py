import asyncio

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Select, ManagedCheckbox, ManagedMultiselect, ManagedRadio
from aiogram.fsm.context import FSMContext
from bot_instans import FSM_ST3, FSM_ST, FSM_ST5
from aiogram_dialog.api.exceptions import OutdatedIntent, NoContextError


async def go_back(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.back()


async def go_next(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.next()



async def go_first(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=FSM_ST.start)


async def go_second(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=FSM_ST.window_2)


async def go_third(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=FSM_ST.window_3)


async def go_fourth(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=FSM_ST.window_4)

# Хэндлер, обрабатывающий нажатие на кнопку 'Да'
async def yes_click_process(callback: CallbackQuery,
                            widget: Button,
                            dialog_manager: DialogManager):
    print('\n\nYes Handler')
    try:
        await callback.message.edit_text(
            text='<b>Прекрасно!</b>\n\nНадеюсь, вы найдете в этом курсе что-то '
                 'новое и полезное для себя!')
    except Exception:
        print('Exeption happend')

    await dialog_manager.done()


# Хэндлер, обрабатывающий нажатие на кнопку 'Нет'
async def no_click_process(callback: CallbackQuery,
                           widget: Button,
                           dialog_manager: DialogManager):
    await callback.message.edit_text(
        text='<b>Попробуйте!</b>\n\nСкорее всего, вам понравится!')
    await dialog_manager.done()

# Хэндлер, обрабатывающий нажатие на кнопку
async def button_clicked(callback: CallbackQuery,
                           widget: Button,
                           dialog_manager: DialogManager):
    """Хэндлер обрабатывающий колбэк с нажатием на кнопку из диалога drei"""
    await callback.message.answer('drei dialog works\n\n Нажмите на кнопку выше 👆')
    await dialog_manager.next()

async def button_clicked_to_five(callback:CallbackQuery, widget:Button, dialog_manager:DialogManager):
    await callback.message.answer('Переходим к диалогу five')
    await dialog_manager.start(state=FSM_ST5.five)


async def category_selection(callback: CallbackQuery, widget: Select,
                             dialog_manager: DialogManager,   item_id: str):
    # print(type(item_id), item_id)
    await callback.message.answer(
        f'Выбрана категория Название {item_id.split()[0]}  с id={item_id.split()[1]}')
    await asyncio.sleep(2)
    await dialog_manager.start(state=FSM_ST3.drei, mode=StartMode.RESET_STACK)





# Хэндлер, обрабатывающий нажатие кнопки в виджете `Checkbox`
async def checkbox_clicked(callback: CallbackQuery, checkbox: ManagedCheckbox,
                           dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(is_checked=checkbox.is_checked())



async def category_filled(callback: CallbackQuery,
                          checkbox: ManagedMultiselect, manager: DialogManager, *args, **kwargs):
    chosen_topics = checkbox.get_checked()
    manager.dialog_data["multi_topics"] = chosen_topics # Вручную обновляю контекст
    print('sel top = ', manager.dialog_data["multi_topics"])  #  sel top =  ['Искусство 6', 'Культура 5']



# Хэндлер, обрабатывающий нажатие на кнопку
async def button_in_six_clicked(callback: CallbackQuery,  widget: Button,dialog_manager: DialogManager):
    """Хэндлер обрабатывающий колбэк с нажатием на кнопку из диалога six"""
    widget = dialog_manager.find('multi_topics')
    data = widget.get_checked()
    selected_topics = dialog_manager.current_context().dialog_data.get("multi_topics")
    print('selected_topics = ', selected_topics)  #  selected_topics =  ['Искусство 6', 'Культура 5']
    state = dialog_manager.middleware_data["state"]  # state получаю из middleware_data, а не из FSMContext
    if selected_topics and len(selected_topics)>1:
        s = ''
        topic_list = []
        for tema in data:
            topic_name = tema.split()[0]
            topic_list.append(topic_name)
            t = '\n\n➡️ ' + topic_name
            s += ''.join(t)
        await callback.message.answer(f'Вы выбрали темы<b>{s}</b>')
        await asyncio.sleep(1)
        await state.update_data(topics=topic_list)
        us_dict = await state.get_data()
        print('us_dict = ', us_dict)  # us_dict = {'topics': ['Искусство', 'Общество']}
        await callback.message.answer("Ваш выбор сохранен!")
        await dialog_manager.done()
    else:
        await callback.message.answer("Выбирите минимум 2 темы !")



async def radio_button_clicked(callback:CallbackQuery,
                           radio: ManagedRadio,
                           dialog_manager: DialogManager, *args, **kwargs):
    selected_language = radio.get_checked()
    state = dialog_manager.middleware_data["state"]
    lan_dict = {'1':'English', '2':'Русский', '3':"Francosic"}

    await state.update_data(lan=lan_dict[selected_language])
    us_dict = await state.get_data()
    print('lan = ', us_dict['lan'])  # lan =  Русский
    await asyncio.sleep(1)
    await dialog_manager.done()  # после этой команды пропадают кнопки
    await asyncio.sleep(1)
    await callback.message.answer(f"Вы выбрали: {us_dict['lan']}")














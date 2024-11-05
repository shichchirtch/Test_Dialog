from aiogram import Router, html, F
import asyncio
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove, User, CallbackQuery
from aiogram.filters import CommandStart, Command, StateFilter
from bot_base import user_dict, users_db
from filters import PRE_START
from lexikon import *
from getters import get_name
from copy import deepcopy
from aiogram.fsm.context import FSMContext
from keyboards import pre_start_clava
from bot_instans import (FSM_ST, FSM_ST2, FSM_ST3, FSM_ST4, FSM_ST5, FSM_ST6, FSM_ST7, FSM_ST_foto,
                         FSM_ST_foto_dinamic, FSM_ST8, FSM_ST9, bot, bot_storage_key, dp)
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs, ShowMode
from random import randint, choice
from contextlib import suppress
from aiogram_dialog.widgets.text import Const, Format, Multi
# from inlinekeyboards import *
from aiogram_dialog.api.exceptions import OutdatedIntent, NoContextError

import pprint


ch_router = Router()

# @ch_router.message(F.photo)
# async def foto_id_geber_messages(message: Message):
#     data = message.photo[-1].file_id
#     print(data)


@ch_router.message(CommandStart(), PRE_START())
async def command_start_process(message:Message, dialog_manager: DialogManager, state:FSMContext):

    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict)
        await state.set_data({'topics':''})
        att = await message.answer(text='👋', reply_markup=ReplyKeyboardRemove())
        try:
            await dialog_manager.start(state=FSM_ST.start, mode=StartMode.RESET_STACK, data={'topics':''})
            print('*** We are here !')
        except NoContextError:
            print('NoContextError: happened')

            await dialog_manager.start(state=FSM_ST.start, mode=StartMode.RESET_STACK)
        await asyncio.sleep(1.5)
        await att.delete()



@ch_router.message(PRE_START())
async def before_start(message: Message, dialog_manager: DialogManager):
    prestart_ant = await message.answer(text='Klicken auf <b>start</b> !',
                                        reply_markup=pre_start_clava)
    await dialog_manager.done()  # Здесь возникает ошибка

    await message.delete()
    await asyncio.sleep(3)
    await prestart_ant.delete()


@ch_router.message(Command('lernen'))
async def command_lernen_process(message:Message, dialog_manager: DialogManager):
    try:
        await dialog_manager.start(state=FSM_ST2.lernen, mode=StartMode.NORMAL)
        print('*** We in second !')
    except OutdatedIntent:
        print('OutdatedIntent happened')

    await asyncio.sleep(5)
    await dialog_manager.done()



@ch_router.message(Command('drei'))
async def command_drei_process(message:Message, dialog_manager: DialogManager):
    try:
        await dialog_manager.start(state=FSM_ST3.drei, mode=StartMode.NORMAL)
        print('*** We in drei !')
    except OutdatedIntent:
        print('OutdatedIntent happened')



@ch_router.message(Command('s_item'))
async def command_s_item_process(message:Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=FSM_ST4.vier, mode=StartMode.NORMAL)
    print('*** We in vier !')



@ch_router.message(Command('five'))
async def command_checkbox_process(message:Message, dialog_manager: DialogManager):
    try:
        await dialog_manager.start(state=FSM_ST5.five, mode=StartMode.NORMAL)
        print('*** We in five !')
    except OutdatedIntent:
        print('OutdatedIntent happened')




@ch_router.message(Command('sex'))
async def command_six_process(message:Message, dialog_manager: DialogManager):
    try:
        await dialog_manager.start(state=FSM_ST6.sex, mode=StartMode.NORMAL)
        print('*** We in sex !')
    except OutdatedIntent:
        print('OutdatedIntent happened')



@ch_router.message(Command('radio'))
async def command_radio_process(message:Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=FSM_ST7.radio, mode=StartMode.NORMAL, show_mode=ShowMode.DELETE_AND_SEND)
    print('*** We in radio !')



@ch_router.message(Command('foto'))
async def send_foto_process(message:Message, dialog_manager: DialogManager):
    try:
        await dialog_manager.start(state=FSM_ST_foto.send_foto, mode=StartMode.NORMAL)
        print('/// We in foto !')
    except OutdatedIntent:
        print('OutdatedIntent happened')

@ch_router.message(Command('photo'))
async def send_photo_process(message:Message, dialog_manager: DialogManager):
    try:
        await dialog_manager.start(state=FSM_ST_foto_dinamic.foto_dinamic, mode=StartMode.NORMAL)
        print('/// We in photo !')
    except OutdatedIntent:
        print('OutdatedIntent happened')

@ch_router.message(Command('get_age'))
async def get_age_process(message:Message, dialog_manager: DialogManager):
    try:
        await dialog_manager.start(state=FSM_ST8.input_text, mode=StartMode.NORMAL)
        print('((( We in get_age !')
    except OutdatedIntent:
        print('OutdatedIntent happened')

@ch_router.message(Command('exo'))
async def exo_process(message:Message, dialog_manager: DialogManager):
    try:
        await dialog_manager.start(state=FSM_ST9.any_content, mode=StartMode.NORMAL)
        print('((( We in exo !')
    except OutdatedIntent:
        print('OutdatedIntent happened')


@ch_router.message(StateFilter(FSM_ST.start))
async def trasher(message: Message):
    print('TRASHER')
    await asyncio.sleep(1)
    await message.delete()























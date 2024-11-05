from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import StorageKey, MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.fsm.state import State, StatesGroup

scheduler = AsyncIOScheduler()

aio_storage = MemoryStorage()

class FSM_ST(StatesGroup):
    start = State()  # FSM_ST:after_start
    admin = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()

class FSM_ST2(StatesGroup):
    lernen = State()

class FSM_ST3(StatesGroup):
    drei = State()
    drei_two = State()

class FSM_ST4(StatesGroup):
    vier = State()

class FSM_ST5(StatesGroup):
    five = State()


class FSM_ST6(StatesGroup):
    sex = State()

class FSM_ST7(StatesGroup):
    radio = State()

class FSM_ST_foto(StatesGroup):
    send_foto = State()

class FSM_ST_foto_dinamic(StatesGroup):
    foto_dinamic = State()

class FSM_ST8(StatesGroup):
    input_text = State()
    get_name = State()

class FSM_ST9(StatesGroup):
    any_content = State()


BOT_TOKEN = '<BOT_TOKEN>'

bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

bot_storage_key = StorageKey(bot_id=bot.id, user_id=bot.id, chat_id=bot.id)

dp = Dispatcher(storage=aio_storage)

bot = Bot(token=BOT_TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
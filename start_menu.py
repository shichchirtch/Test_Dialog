from aiogram.types import BotCommand

async def set_main_menu_2(bot):

    main_menu_commands_2 = [
        BotCommand(command='/s_item',
                   description='Select'),

        BotCommand(command='/drei',
                   description='test'),

        BotCommand(command='/lernen',
                   description='test'),

        BotCommand(command='/five',
                   description='checkbox'),

        BotCommand(command='/sex',
                   description='multiSekect'),

        BotCommand(command='/get_age',
                   description='Ваш возраст'),

        BotCommand(command='/radio',
                   description='демонстрация виджета'),

        BotCommand(command='/exo',
                   description='start with s')
    ]

    await bot.set_my_commands(main_menu_commands_2)


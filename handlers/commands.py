from aiogram import Router
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from Tbot_beahea.keyboards import kb
from Tbot_beahea.data import db_funcs, text
from Tbot_beahea.states.states import StateUserProfile

router = Router()



@router.message(Command('start'))
async def reg_profile(msg: Message, state: FSMContext):
    """
    Реагирует на команду 'start'. При вызове проверяет на наличие юзера.
    Если юзера нет записывает данные пользователя в БД.
    Если есть, предлагает обнулить данные.

    :param msg:
    :param state:
    :return:
    """

    user_id = msg.from_user.id
    await msg.answer(text.greet.format(name=msg.from_user.id))
    if db_funcs.check_user_datas(user_id=user_id):
        await msg.answer(text=f'Вы уже зарегистрированы.',
                         reply_markup=kb.user_profile(user_id=msg.from_user.id),
                         )
        await msg.answer(text=f'Хотите очистить профиль?.',
                         reply_markup = kb.choiceYN(text.clear_account_question),
                         )
        await state.set_state(StateUserProfile.clear_profile)

    else:
        acc_dict = {
            'user_id': msg.from_user.id,
            'name': msg.from_user.first_name,
            'surname': msg.from_user.last_name,
            'username': msg.from_user.username
        }
        db_funcs.user_rec_datas_in_reg(acc_dict)
        if db_funcs.check_user_datas(user_id):
            await msg.answer('Был автоматически создан профиль!')
            await msg.answer(text=text.menu, reply_markup=kb.main_menu())
        else:
            await msg.answer('Произошла критическая ошибка при регистрации. Уведомите пожалуйста администратора.\n'
                             'Следующее сообщение будет отправлено администратору.')
            prompt = msg.text
            await msg.answer(prompt)

@router.message()
async def set_commands(bot: BotCommand):
    commands = [
        BotCommand(command="/drinks", description="Заказать напитки"),
        BotCommand(command="/food", description="Заказать блюда"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)

@router.message(Command('menu'))
async def menu_handler(msg: Message, state: FSMContext):
    await msg.answer(text.menu,
                     reply_markup=kb.main_menu())




@router.message(Command('help'))
async def send_help(msg: Message):
    await msg.answer(text="""
Вот список команд для использования:
/start - Запуск бота. Автоматически создается аккаунт. При повторном вызове предлагает сбросить профиль.
/help - Список команд
/info - вызов чата со службой поддержки.
Обратите внимание! Тех. поддержка не отвечает на вопросы медицины, нутрициологии и "какие БАД посоветовать".

""",
                     reply_markup=kb.main_menu())
from aiogram import F, Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils.media_group import MediaGroupBuilder

from datas.models.models_user import AdminList, User, Admin
from datas.models.models_basic_data import UserBasicData
from datas.models.models_db import db_beahea
from datas.texts import text, text_admin_navigator, text_of_paid_service, text_user_questions
from config.config import ADMIN_DIMA

from states.states import StateMenu, StateAdminMenu, StateUserProfile
from keyboards import kb_main_menu, kb_pay_menu
from keyboards.kb_admin import kb_admin_menu
from keyboards.kb_user import kb_user_profile
from handlers.required import admin_required, user_required

router = Router()


@router.message(CommandStart())
async def handler_start(msg: Message, state: FSMContext, bot: Bot):
    """
    Реагирует на команду 'start'. При вызове проверяет на наличие юзера.
    Если юзера нет записывает данные пользователя в БД.
    Если есть, предлагает обнулить данные.


    :param msg: Сообщение от пользователя
    :param state: Состояние бота

    """

    user_id = msg.from_user.id
    username = msg.from_user.username
    surname = msg.from_user.last_name
    name = msg.from_user.first_name
    user = User.check_user_datas(user_id=user_id)
    if user:
        await msg.answer(text=text.greet_cont_replay.format(name=msg.from_user.first_name),
                         reply_markup=kb_main_menu.main_menu(user_id=user_id))
        await state.set_state(StateMenu.main_menu)

    else:
        acc_dict = {
            'user_id': user_id,
            'name': name,
            'surname': surname,
            'username': username
        }
        with db_beahea.atomic():
            User.create(**acc_dict)
            UserBasicData.create(**acc_dict)

        if User.check_user_datas(user_id):
            check_admin_user_user_id = AdminList.select().where(AdminList.user_id == user_id)
            check_admin_user_username = AdminList.select().where(AdminList.username == username)
            if check_admin_user_user_id:
                check_admin_user = check_admin_user_user_id.get()
                check_admin_username = check_admin_user.username
                if check_admin_username is None:
                    adm = AdminList.update(username=username).where(Admin.user_id == user_id)
                    adm.execute()
            elif check_admin_user_username:
                check_admin_user = check_admin_user_username.get()
                check_admin_user_id = check_admin_user.user_id
                if check_admin_user_id is None:
                    adm = Admin.update(user_id=user_id).where(AdminList.username == username)
                    adm.execute()
            await msg.answer(text=text.greet_cont.format(name=name),
                             reply_markup=kb_main_menu.main_menu(user_id=user_id))
            await state.set_state(StateMenu.main_menu)
        else:
            await msg.answer(text=text.err_reg_fatal)
            prompt = msg.text
            await bot.send_message(chat_id=ADMIN_DIMA, text=prompt)


@router.message(Command('main_menu'))
@router.message(F.text.lower().in_({"выйти в меню", 'главное меню'}))
@user_required
async def f_main_menu(msg: Message, state: FSMContext, bot: Bot):
    await state.clear()
    user_id = msg.from_user.id
    await msg.answer(text=text.main_menu, reply_markup=kb_main_menu.main_menu(user_id=user_id))
    await state.set_state(StateMenu.main_menu)


@router.message(StateMenu.main_menu)
@admin_required
@user_required
async def main_menu(msg: Message, state: FSMContext, bot: Bot):
    user_id = msg.from_user.id
    prompt = msg.text
    if prompt == "Меню администратора":
        await msg.answer(text_admin_navigator.admin_main_menu,
                         reply_markup=kb_admin_menu.admin_main_menu(user_id=user_id))
        await state.set_state(StateAdminMenu.admin_main_menu)


@user_required
async def t_channel(msg: Message, state: FSMContext, bot: Bot):
    caption = '''могу сделать так. Передается видео с подписью и кнопкой. Подпись по моему безгранична'''

    await msg.answer_video(video='https://t.me/beahea_public/391', caption=caption,
                           reply_markup=kb_pay_menu.go_to_telegram_channel())
    await msg.answer(text='Разделение для наглядности')
    caption = """Или так \n Межпозвоночные диски и суставы не имеют прямого кровоснабжения, как многие другие части тела, и поэтому они питаются иначе — через процесс, называемый диффузией. 

✅ Этот процесс происходит при помощи сдавливания и последующего расслабления, которое возникает в результате движения и физической активности."""
    await msg.answer_photo(photo='https://t.me/beahea_public/399', caption=caption,
                           reply_markup=kb_pay_menu.go_to_telegram_channel())
    await msg.answer(text='Разделение')
    caption = ("""Еще так могу.\n
    Когда в одном сообщении надо отправить несколько, фото, доков или видео или их коллаб, то нельзя передавать кнопку вместе с ними. кнопки можно передать юзеру для нажатия
    только с одним видео или одной фотографией.
    \n
        
               """)
    media_group = MediaGroupBuilder(caption=caption)
    media_group.add_video(media='https://t.me/beahea_public/390')
    media_group.add_photo(media='https://t.me/beahea_public/385')
    media_group.add_photo(media='https://t.me/beahea_public/388')
    media_group.add_video(media='https://t.me/beahea_public/387')

    await msg.answer_media_group(media_group.build())
    await msg.answer(text='Тут обязательно должно быть какое нибудь сообщение, иначе кнопку не передать',
                     reply_markup=kb_pay_menu.go_to_telegram_channel())


@user_required
async def send_to_Elya(msg: Message, state: FSMContext, bot: Bot):
    pass


@user_required
async def marathon(msg: Message, state: FSMContext, bot: Bot):
    user = User.get(User.user_id == msg.from_user.id)
    accept = user.subscribe_marathon
    if accept:
        await msg.answer(text=text_of_paid_service.subscribe_marathon_paid_for,
                         reply_markup=kb_pay_menu.go_to_marathon_channel())
    else:
        await msg.answer(text=text_of_paid_service.subscribe_marathon_not_paid_for,
                         reply_markup=kb_pay_menu.not_go_to_marathon_channel())
    await state.set_state(StateMenu.main_menu)


@user_required
async def private_channel(msg: Message, state: FSMContext, bot: Bot):
    user = User.get(User.user_id == msg.from_user.id)
    accept = user.subscribe_on_private_channel
    if accept:
        await msg.answer(text=text_of_paid_service.subscribe_private_channel_paid_for,
                         reply_markup=kb_pay_menu.go_to_private_telegram_channel())
        await state.set_state(StateMenu.main_menu)

    else:
        await msg.answer(text=text_of_paid_service.subscribe_private_channel_not_paid_for,
                         reply_markup=kb_pay_menu.not_go_to_private_telegram_channel())
        await state.set_state(StateMenu.main_menu)


@user_required
async def profile(msg: Message, state: FSMContext, bot: Bot):
    """
    Меню аккаунта
    """
    await msg.answer(text='Главное меню профиля, че нить написать', reply_markup=kb_user_profile.user_profile())
    await state.set_state(StateMenu.user_profile)


@router.message(StateMenu.user_profile)
@user_required
async def user_profile(msg: Message, state: FSMContext, bot: Bot):
    prompt = msg.text
    for key, value in text_user_questions.user_profile.items():
        if prompt == value[0]:
            next_state = getattr(StateUserProfile, key)
            text_mess = value[1]
            kb = getattr(kb_user_profile, key)
            await state.set_state(next_state)
            await msg.answer(text=text_mess, reply_markup=kb(user_id=msg.from_user.id))
            break


async def send_help(msg: Message, state: FSMContext):
    await msg.answer(text="Вот список команд для использования")
    await msg.answer(text="""
/start - Запуск бота.
/main_menu - Главное меню.
/profile - Данные профиля.
/help - Список команд.
""",
                     reply_markup=kb_main_menu.main_menu(user_id=msg.from_user.id))
    await state.set_state(StateMenu.main_menu)

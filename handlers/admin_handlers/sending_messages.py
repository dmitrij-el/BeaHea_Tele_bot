import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from aiogram import Router, Bot
from aiogram.types import Message

from datas.models.models_db import db_beahea
from datas.models.models_user import AdminList

router = Router()


def gives_admins():
    """Возвращает список ID администраторов."""
    with db_beahea:
        return [adm.user_id for adm in AdminList.select() if adm.user_id is not None]

async def notification_reservations_today(msg: Message, notification: str):
    """Отправляет уведомление всем администраторам."""
    try:
        # Получаем список ID администраторов
        admin_ids = gives_admins()
        for admin_id in admin_ids:
            await msg.bot.send_message(chat_id=admin_id, text=notification)
    except Exception as exp:
        logging.error(
            f'В процессе рассылки после заказа стола/корпоратива произошла ошибка\n'
            f'Ошибка: {exp}'
        )


async def notification_reservations(bot: Bot, admin_id: int):
    pass
    # answer_table = await db_funcs_admin_menu.load_table_reservations(date=datetime.now())
    # await bot.send_message(chat_id=admin_id, text='Резервы столов на сегодня')
    # for ans in answer_table:
    #     await bot.send_message(chat_id=admin_id, text=ans)
    # answer_party = await db_funcs_admin_menu.load_party_reservations(date=datetime.now())
    # await bot.send_message(chat_id=admin_id, text='Резервы корпоративов на сегодня')
    # for ans in answer_party:
    #     await bot.send_message(chat_id=admin_id, text=ans)


def scheduler_args(bot: Bot, scheduler: AsyncIOScheduler):
    admin_ids = gives_admins()
    for adm_id in admin_ids:
        scheduler.add_job(notification_reservations, 'cron', hour=14, minute=00, args=(bot, adm_id))

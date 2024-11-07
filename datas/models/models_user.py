# import datetime
# import logging
#
#
#
#
# class User(BaseUserModel):
#     id = PrimaryKeyField(unique=True)
#     creation_time = DateTimeField(default=datetime.datetime.now)
#     user_id = CharField(unique=True)
#     username = CharField(null=True)
#     is_active = BooleanField(default=True)
#
#     # subscribe_marathon = ForeignKeyField(SubscribeMarathon, backref='user', null=True)
#     # subscribe_private_channel = ForeignKeyField(SubscribePrivateChannel, backref='user', null=True)
#     #
#     # the_basic_data = ForeignKeyField(UserBasicData, backref='user', null=True)
#     # the_body_parameters = ForeignKeyField(UserBodyParameters, backref='user', null=True)
#     # the_questionnaire = ForeignKeyField(UserQuestionnaire, backref='user', null=True)
#
#     class Meta:
#         db_table = "user"
#
#     @classmethod
#     def get_as_dict(cls, user_id):
#         query = cls.select().where(user_id == user_id).dicts()
#         return query.get()
#
#     @classmethod
#     def get_user_by_id(cls, user_id) -> int:
#         return cls.get_or_none(cls.user_id == user_id)
#
#     @classmethod
#     def check_user_datas(cls, user_id: int) -> bool:
#         """
#         Проверка БД на наличие пользователя
#
#         :param user_id: ID пользователя
#         :return: True если юзера есть в БД, иначе False
#         """
#         try:
#             with db_beahea:
#                 return cls.select().where(cls.user_id == user_id).exists()
#         except Exception as exp:
#             logging.error(f'В процессе проверки на наличие пользователя произошла непредвиденная ошибка\n'
#                           f'Ошибка: {exp}')
#             return False
#
#     @classmethod
#     def user_rec_datas_in_reg(cls, acc_dict: dict) -> None:
#         """Запись данных профиля в БД при регистрации
#
#         :param acc_dict: Данные профиля
#         :return: None
#         """
#         try:
#             with db_beahea.atomic():
#                 cls.create(**acc_dict)
#
#
#         except Exception as exp:
#             logging.error(f'В процессе записи пользователя {acc_dict["user_id"]} в БД произошла непредвиденная ошибка\n'
#                           f'Ошибка: {exp}')
#
#
# class Admin(User):
#     class Meta:
#         db_table = "admin"
#
#
#
#
# class AdminList(BaseUserModel):
#     id = PrimaryKeyField(unique=True)
#     user_id = CharField(null=True)
#     username = CharField(null=True)
#
#     class Meta:
#         db_table = "admin_list"
#
#     @classmethod
#     async def load_admin_list(cls) -> list[str]:
#         try:
#             datas = AdminList.select()
#             if datas:
#                 answer = []
#                 for data in datas:
#                     answer.append('')
#                     admin_id = data.id
#                     user_id = data.user_id
#                     username = data.username
#                     answer[-1] += f'ID записи: {admin_id}'
#                     answer[-1] += f'\nID пользователя: {user_id}'
#                     answer[-1] += f'\nUSERNAME пользователя: {username}'
#                     user = User.select().where(User.user_id == user_id)
#                     if user:
#                         user = user.get()
#                         answer[-1] += f'\nДанные о {user.name}'
#                         answer[-1] += f'\nНик: @{user.username}'
#                         gender = user.gender
#                         date_birth = user.date_birth
#                         phone = user.phone
#                         if phone is not None:
#                             answer[-1] += f'\nТелефон: {phone}'
#                         if gender is not None:
#                             answer[-1] += f'\nПол: {user.gender.symbol}'
#                         if date_birth is not None:
#                             date_birth = date_birth.date()
#                             answer[-1] += f'\nДень рождения: {date_birth}'
#                 if len(answer) != 0:
#                     return answer
#                 else:
#                     return ['Администраторов не найдено.']
#             else:
#                 return ['Администраторов не найдено.']
#         except Exception as exp:
#             logging.error(f'В процессе загрузки списка администраторов произошла непредвиденная ошибка\n'
#                           f'Ошибка: {exp}')
#
#
# class SubscribeMarathon(BaseUserModel):
#     user_id = ForeignKeyField(User, backref='subscribe_marathon')
#     id = PrimaryKeyField(unique=True)
#     name = CharField(null=True)
#     creation_time = DateTimeField(default=datetime.datetime.now)
#     subscribe_on_marathon = BooleanField(default=False)
#     date_start_subscribe_marathon = DateTimeField(null=True)
#     date_end_subscribe_marathon = DateTimeField(null=True)
#
#
# class SubscribePrivateChannel(BaseUserModel):
#     user_id = ForeignKeyField(User, backref='subscribe_private_channel')
#     id = PrimaryKeyField(unique=True)
#     name = CharField(null=True)
#     creation_time = DateTimeField(default=datetime.datetime.now)
#     subscribe_on_private_channel = BooleanField(default=False)
#     date_start_subscribe_private_channel = DateTimeField(null=True)
#     date_end_subscribe_private_channel = DateTimeField(null=True)

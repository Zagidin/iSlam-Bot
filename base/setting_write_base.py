from fsm.admins import DeleteUsers
from aiogram.dispatcher import FSMContext
from base.base_users import (
    select_all_users,
    select_admin_users_sms,
    delete_admin_users

)


def write_base_settings():
    user_id = [item[0] for item in select_all_users()]

    return user_id


def delete_user_base_settings():
    for user in select_admin_users_sms():
        delete_admin_users(user[0])

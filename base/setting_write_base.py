from base.base_users import (
    select_all_users,
    select_admin_users_sms
)


def write_base_settings():
    user_id = [item[0] for item in select_all_users()]

    return user_id


def print_users_settings():
    users_sms = [item[0] for item in select_admin_users_sms()]
    len_users = len(users_sms)

    return users_sms, len_users

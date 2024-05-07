from base.base_users import select_all_users


def write_base_settings():
    user_id = [item[0] for item in select_all_users()]

    return user_id

import sqlite3


def start_base():
    db = sqlite3.connect('./base/users.db')
    cur = db.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        id_user INTEGER,
        name TEXT,
        phone INTEGER,
        sms_user TEXT
        )
    """)

    db.close()


def open_write_base_users(id_user, name, phone, sms_user):
    db = sqlite3.connect('./base/users.db')
    cur = db.cursor()

    sql = "INSERT INTO Users (id_user, name, phone, sms_user) VALUES (?, ?, ?, ?)"

    params = (id_user, name, phone, sms_user, )

    cur.execute(sql, params)

    db.commit()
    db.close()


def select_all_users():
    db = sqlite3.connect('./base/users.db')
    cur = db.cursor()

    sql = "SELECT id_user FROM Users"
    cur.execute(sql)
    users_id = cur.fetchall()

    return users_id


def select_admin_users_sms():
    db = sqlite3.connect('./base/users.db')
    cur = db.cursor()

    sql = "SELECT id, name, phone, sms_user FROM Users"
    cur.execute(sql)
    users_sms = cur.fetchall()

    return users_sms

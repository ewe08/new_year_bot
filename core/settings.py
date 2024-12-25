from dataclasses import dataclass

from environs import Env

@dataclass
class Bots:
    bot_token: str


@dataclass
class DataBase:
    """Настройки для базы данных"""
    host:     str
    port:     int
    database: str
    user:     str
    password: str
    ssl:      str


@dataclass
class Settings:
    bots:      Bots
    databases: DataBase
    admins:    set
    givers:    set
    callers:   set


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    admins = {int(i) for i in env.str('ADMINS').split()}
    givers = {int(i) for i in env.str('GIVERS').split()}
    callers = {int(i) for i in env.str('CALLERS').split()}

    return Settings(
        bots=Bots(
            bot_token=env.str('TOKEN'),
        ),
        databases=DataBase(
            host=env.str('HOST'),
            port=env.int('PORT'),
            database=env.str('DATABASE'),
            user=env.str('DBUSER'),
            password=env.str('PASSWORD'),
            ssl=env.str('PATH_TO_SSL'),
        ),
        admins=admins,
        givers=givers | admins,
        callers=callers | admins,
    )


settings = get_settings('.env')

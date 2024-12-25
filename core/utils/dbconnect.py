import ssl
import aiomysql

from core.settings import settings


ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.load_verify_locations(cafile=settings.databases.ssl)


async def create_pool(loop):
    """Подключение базы данных"""
    return await aiomysql.create_pool(
        user=settings.databases.user,
        password=settings.databases.password,
        db=settings.databases.database,
        host=settings.databases.host,
        port=settings.databases.port,
        ssl=ctx,
        loop=loop,
    )


def double_quote(string):
    if string is None:
        return string
    return string.replace("'", "''")


class Request:
    def __init__(self, connector: aiomysql.Connection):
        self.connection = connector
        self._table = 'userdata'
        self.tickets_table = 'tickets'

    async def register_user(self, user_id, username):
        query = f"INSERT INTO {self._table} (id, username, score) " \
                f"VALUES ({user_id}, '{double_quote(username)}', 15)"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query)
            await self.connection.commit()  # Подтверждение изменений

    async def get_score(self, user_id):
        query = f"SELECT score FROM {self._table} WHERE id={user_id}"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, ())
            result = await cursor.fetchall()

        if result:
            return result  # Возвращаем пользователей
        return None  # Возвращаем None, если результат пустой

    async def get_username(self, user_id):
        query = f"SELECT username FROM {self._table} WHERE id={user_id}"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, ())
            result = await cursor.fetchall()

        if result:
            return result  # Возвращаем пользователей
        return None  # Возвращаем None, если результат пустой

    async def check_username(self, username):
        query = f"SELECT (id) FROM {self._table} " \
                f"WHERE username='{double_quote(username)}'"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, ())
            result = await cursor.fetchall()

        if result:
            return result  # Возвращаем пользователей
        return None  # Возвращаем None, если результат пустой

    async def update_username(self, user_id, username):
        query = f"UPDATE {self._table} " \
                f"SET username = '{double_quote(username)}' " \
                f"WHERE id={user_id}"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query)
            await self.connection.commit()

    async def give_score_by_username(self, username, value):
        query = f"UPDATE {self._table} " \
                f"SET score = score + %s " \
                f"WHERE username = %s"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, (value, username))
            await self.connection.commit()

    async def take_score_by_username(self, username, value):
        query = f"UPDATE {self._table} " \
                f"SET score = score - %s " \
                f"WHERE username = %s"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, (value, username))
            await self.connection.commit()

    async def buy_ticket(self, user_id):
        query = f"INSERT INTO {self.tickets_table} (user_id) VALUES (%s)"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, (user_id,))
            await self.connection.commit()  # Подтверждение изменений
            await cursor.execute("SELECT LAST_INSERT_ID()")  # Получение последнего ID
            ticket_id = await cursor.fetchone()
            return ticket_id[0]  # Возврат ID

    async def take_score_by_user_id(self, user_id, value):
        query = f"UPDATE {self._table} " \
                f"SET score = score - %s " \
                f"WHERE id=%s"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, (value, user_id))
            await self.connection.commit()

    async def get_tickets(self, user_id):
        query = f"SELECT (id) FROM {self.tickets_table} " \
                f"WHERE user_id=%s"
        async with self.connection.cursor() as cursor:
            await cursor.execute(query, (user_id,))
            result = await cursor.fetchall()

        if result:
            return result  # Возвращаем пользователей
        return None  # Возвращаем None, если результат пустой

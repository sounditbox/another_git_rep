import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

import psycopg
from psycopg_pool import AsyncConnectionPool

# from psycopg_pool import ConnectionPool

db_params = {
    "dbname": "my_db2",  # Имя базы данных
    "user": "postgres",  # Имя пользователя
    "password": "postgres",  # Пароль
}
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())


async def main():
    async with AsyncConnectionPool('host=localhost port=5432 dbname=my_db2 user=postgres password=postgres', max_size=10) as pool:
        async with pool.connection() as aconn:
            async with aconn.cursor() as acur:
                await acur.execute("SELECT * FROM orders")
                async for record in acur:
                    print(record)


asyncio.run(main())

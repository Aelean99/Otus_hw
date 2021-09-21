"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List

from jsonplaceholder_requests import get_users_data, get_posts_data
from models import _AsyncSession, async_engine, Decl_base, User, Post


async def create_tables():
    async with async_engine.begin() as engine:
        await engine.run_sync(Decl_base.metadata.create_all)


async def my_insert(to_table, data: List[dict]):
    async with _AsyncSession() as session:
        ready_list = [to_table(**i) for i in data]
        session.add_all(ready_list)


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(get_users_data(), get_posts_data())
    await asyncio.gather(my_insert(to_table=User, data=users_data),
                         my_insert(to_table=Post, data=posts_data))


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

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

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import fetch_users, fetch_posts
from homework_04.models import engine, Base, User, Post, async_session


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(users_data: List[User]) -> List[User]:
    users = [
        User(name=item["name"], username=item["username"], email=item["email"])
        for item in users_data
    ]
    async with async_session() as session:  # type: AsyncSession
        async with session.begin():
            session.add_all(users)
    return users


async def create_posts(posts_data: List[Post]) -> List[Post]:
    posts = [
        Post(user_id=item["userId"], title=item["title"], body=item["body"])
        for item in posts_data
    ]
    async with async_session() as session:  # type: AsyncSession
        async with session.begin():
            session.add_all(posts)

    return posts


async def async_main():
    await create_table()
    users_data, posts_data = await asyncio.gather(
        fetch_users(),
        fetch_posts(),
    )
    await create_users(users_data)
    await create_posts(posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

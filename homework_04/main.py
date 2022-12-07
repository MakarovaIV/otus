"""
Домашнее задание №4
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
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)

from homework_04.models import User
from homework_04.models import Post
from homework_04.models import Base
from homework_04.models import Session, async_engine
from homework_04.jsonplaceholder_requests import get_users_data, get_posts_data


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session: AsyncSession, users_data: list) -> list[User]:
    user_list = [
        User(username=usr['username'], name=usr['name'], email=usr['email'])
        for usr in users_data
    ]
    session.add_all(user_list)
    await session.commit()

    return user_list


async def create_posts(session: AsyncSession, user_list: list[User], posts_data: list) -> list[Post]:
    posts = []
    for usr in user_list:
        user_posts = list(filter(lambda pst: pst['userId'] == usr.id, posts_data))
        posts_list = [
            Post(title=pst['title'], body=pst['body'], user=usr)
            for pst in user_posts
        ]
        posts += posts_list

    session.add_all(posts)
    await session.commit()

    return posts


async def async_main():
    await create_tables()

    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        get_users_data(),
        get_posts_data(),
    )

    async with Session() as session:
        user_list = await create_users(session, users_data)
        await create_posts(session, user_list, posts_data)


async def main():
    await async_main()


if __name__ == '__main__':
    asyncio.run(main())

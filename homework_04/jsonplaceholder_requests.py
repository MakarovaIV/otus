"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import json

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_json(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        return data


async def get_users_data():
    return await get_json(USERS_DATA_URL)


async def get_posts_data():
    return await get_json(POSTS_DATA_URL)

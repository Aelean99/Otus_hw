"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url):
    async with ClientSession() as client:
        result = await client.get(url=url)
        return await result.json()


async def get_users_data():
    return await fetch_json(USERS_DATA_URL)


async def get_posts_data():
    return await fetch_json(POSTS_DATA_URL)

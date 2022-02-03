"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import logging
import asyncio

from aiohttp import ClientSession


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_posts() -> dict:
    logging.info(f"Get posts from {POSTS_DATA_URL}")
    async with ClientSession() as session:
        result = await fetch_json(session, POSTS_DATA_URL)
    logging.info(f"get result from json from {POSTS_DATA_URL}: {result}")
    return result


async def fetch_users() -> dict:
    logging.info(f"Get users from {USERS_DATA_URL}")
    async with ClientSession() as session:
        result = await fetch_json(session, USERS_DATA_URL)
    logging.info(f"get result from {POSTS_DATA_URL}: {result}")
    return result


async def main():
    await asyncio.gather(fetch_users(), fetch_posts())


if __name__ == "__main__":
    asyncio.run(main())


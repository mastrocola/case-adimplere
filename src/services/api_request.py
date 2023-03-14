import asyncio
import aiohttp


async def get_data(session, url):
    async with session.get(url) as response:
        return await response.json()


async def api_request(urls):
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*[get_data(session, url) for url in urls])

    return [{**obj} for response in responses for obj in response]

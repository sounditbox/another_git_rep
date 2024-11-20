import aiohttp
import asyncio


async def fetch_page(url):
    async with aiohttp.ClientSession() as session, session.get(url) as response:
        return await response.text()


async def main():
    html = await fetch_page('https://api.github.com/users/sounditbox')
    print(html)


asyncio.run(main())

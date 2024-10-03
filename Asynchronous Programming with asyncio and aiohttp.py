#Asynchronous Programming with asyncio and aiohttp
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

urls = ['https://example.com', 'https://httpbin.org/get', 'https://jsonplaceholder.typicode.com/todos/1']
result = asyncio.run(fetch_all(urls))
for i, content in enumerate(result):
    print(f"Content from {urls[i]}:\n{content[:100]}\n")

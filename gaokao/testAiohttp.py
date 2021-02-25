import aiohttp
import asyncio
from datetime import datetime


async def fetch(client):
    print("打印 ClientSession 对象")
    print(client)
    headers = {'content-type': 'application/json', 'User-Agent': 'Python/3.7 aiohttp/3.7.2'}
    async with client.get('http://httpbin.org/get',headers=headers, timeout=60) as resp:
        assert resp.status == 200
        return await resp.json()


async def main():
    async with aiohttp.ClientSession() as client:
       tasks = []
       for i in range(30):
           tasks.append(asyncio.create_task(fetch(client)))
       await asyncio.wait(tasks)

loop = asyncio.get_event_loop()

start = datetime.now()

loop.run_until_complete(main())

end = datetime.now()
print("aiohttp版爬虫花费时间为：")
print(end - start)



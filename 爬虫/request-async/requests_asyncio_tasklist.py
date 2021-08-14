import asyncio
from multiprocessing.dummy import Pool
import multiprocessing as mp
import time

import aiohttp as aiohttp
import requests


#  多任务， 协程，aiohttp 应用
async def request(str):
    print("下载ing", str)
    # 异步中出现同步，无法实现异步,真实场景request也同步，
    # 需要替换为aiohttp：基于异步网络请求模块
    async with aiohttp.ClientSession() as session:
        async with await session.get(str) as respose:
            # 异步执行时一定加await手动挂起
            page_text = await respose.text()
            print(page_text)

    # time.sleep(2)
    # asyncio 中阻塞操作手动挂起
    await asyncio.sleep(2)
    print("下载success", str)
    return str


start_time = time.time()
urls = ['https://www.baidu.com', 'https://www.sogou.com', 'https://www.360.com']

list_task = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    list_task.append(task)

loop = asyncio.get_event_loop()
# 任务列表封装到wait
loop.run_until_complete(asyncio.wait(list_task))

end_time = time.time()
print('耗时', end_time - start_time)

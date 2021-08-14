import asyncio
from multiprocessing.dummy import Pool
import multiprocessing as mp
import time
import requests

#  多线程进阶-最佳实践-协程的应用

start_time = time.time()

# cpu 个数，最大线程池利用创建
print("Number of cup", mp.cpu_count())


async def request(str):
    print("下载ing", str)
    time.sleep(2)
    print("下载success", str)
    return str

# async 修饰的函数，调用后，返回协程对象
c = request('www.baidu.com')

'''

# 创建事件循环对象
loop = asyncio.get_event_loop()
# 注册并完成启动
loop.run_until_complete(c)
'''
'''
# task 使用
loop = asyncio.get_event_loop()
task = loop.create_task(c)
print(task)
loop.run_until_complete(task)
print(task)
'''


# future的 使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# 绑定回调
def callback_func(task):
    print("task回调值"+task.result())


loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
task.add_done_callback(callback_func)
loop.run_until_complete(task)

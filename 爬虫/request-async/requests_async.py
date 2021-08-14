from multiprocessing.dummy import Pool
import multiprocessing as mp
import time
import requests

#  多线程，多进程无法无限制开启多线程
#  线程池的创建

start_time = time.time()

# cpu 个数，最大线程池利用创建
print("Number of cup", mp.cpu_count())


def get_page(str):
    print("下载ing", str)
    time.sleep(2)
    print("下载success", str)


name_list = ["file1", "file2", "file3", "file5", "file6", "file7", "file8", "file9",
             "file1", "file2", "file3", "file5", "file6", "file7", "file8", "file9"]

# 创建线程池
pool = Pool(mp.cpu_count())
# 将列表参数传递给get_page()
# pool.map(),同步执行
pool.map(get_page, name_list)
# 扩展pool.map_async()异步执行，详细查询api 差异
#pool.map_async(get_page, name_list)
end_time = time.time();
print("耗时", end_time - start_time)

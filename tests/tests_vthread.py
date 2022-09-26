import time, random, queue
from vthread import pool, lock

ls = queue.Queue()
producer = 'pr'
consumer = 'co'

@pool(6, gqueue=producer)
def creater(num):
    time.sleep(random.random()) # 随机睡眠 0.0 ~ 1.0 秒
    print("数据进入队列: {}".format(num))
    ls.put(num)
@pool(1, gqueue=consumer)
def coster():
    # 这里之所以使用 check_stop 是因为，这里需要边生产边消费
    while not pool.check_stop(gqueue=producer):
        time.sleep(random.random()) # 随机睡眠 0.0 ~ 1.0 秒
        pp = [ls.get() for _ in range(ls.qsize())]
        print('当前消费的列表 list: {}'.format(pp))

for i in range(30): creater(i)
coster() # 写作逻辑限制了这里的数量
pool.wait(gqueue=producer) # 等待默认的 gqueue=producer 组线程池全部停止再执行后面内容
pool.wait(gqueue=consumer) # 等待默认的 gqueue=consumer 组线程池全部停止再执行后面内容
print('当生产和消费的任务池数据都结束后，这里才会打印')
print('current queue size:{}'.format(ls.qsize()))
print('end')
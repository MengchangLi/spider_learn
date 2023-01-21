import time
from multiprocessing.dummy import Pool

def get_page(str):
    print("正在下载" + str)
    time.sleep(2)
    print("下载成功" + str)

if __name__ == '__main__':
    start_time = time.time()

    name_list = ['xia', 'aa', 'nn', 'cc']

    pool = Pool(4)
    # 将列表中每一个对象传递给get_page处理
    pool.map(get_page, name_list)

    end_time = time.time()

    print(end_time - start_time)
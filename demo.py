import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
    # 计算总和，这里只是为了消耗时间
    result_item = count(x)
    # 打印输入和输出结果
    return result_item


def count(number):
    for i in range(0, 10000000):
        i = i + 1
    return i * number


if __name__ == "__main__":
    # 线程池执行
    start_time_1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print('result', future.result())
    print("Thread pool execution in " + str(time.time() - start_time_1), "seconds")

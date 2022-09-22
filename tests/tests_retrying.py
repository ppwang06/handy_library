"""
retrying 模块使用
参数说明
"""
from retrying import retry


@retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=3000)
def run():
    print("开始重试")
    raise NameError


# def run2(exception):
#     print(isinstance(exception, ZeroDivisionError))
#     return isinstance(exception, ZeroDivisionError)
#
#
# @retry(retry_on_exception=run2)
# def run():
#     print("开始重试")
#     a = 1 / 0


if __name__ == '__main__':
    run()



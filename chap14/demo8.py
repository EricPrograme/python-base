# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/27 17:23


"""
 第三方插件的安装与使用

 定时任务
"""

import schedule
import time


def job():
    print("哈哈哈，时间流逝-----------")


# 每3s执行以下job函数
schedule.every(3).seconds.do(job)

while True:
    print(time.gmtime().tm_sec)
    schedule.run_pending()
    # 休眠1s
    time.sleep(1)


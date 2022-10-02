# coding=utf-8

"""
0.0.0.220904_alpha, by XPC
"""

import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(threadName)s - %(message)s"
                    ,datefmt="%Y-%m-%d %H:%M:%S"
                    )
import threading
import time

from Get_SensorData import main as get_sensor_data


class RepeatingTimer(threading.Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)

def main():
    flag_getSensorData=True
    # TODO 定时循环读取读取传感器数据
    Thread1 = RepeatingTimer(10.0, get_sensor_data)
    Thread1.start()


    # Thread1.cancel()



    # TODO 将读取数据存入数据库(或写入CSV？)
    # TODO 线程2实时动态显示数据
    # TODO 生成报表





if __name__ == '__main__':
    main()



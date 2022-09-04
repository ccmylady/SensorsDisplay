# coding=utf-8

"""
0.0.0.220904_alpha, by XPC
"""

import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s"
                    ,datefmt="%Y-%m-%d %H:%M:%S"
                    )
import threading

from Modbus_TCP_master import main as read_sensor_data


def main():
    # TODO 线程1读取传感器数据
    threadObj=threading.Thread(target=read_sensor_data)
    threadObj.start()
    # TODO 将读取数据存入数据库(或写入CSV？)
    # TODO 线程2实时动态显示数据
    # TODO 生成报表





if __name__ == '__main__':
    main()



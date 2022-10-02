#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python
 modified 220903 by XPC
"""

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp
import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(threadName)s - %(message)s"
                    ,datefmt="%Y-%m-%d %H:%M:%S"
                    )

def main():
    """main"""
    datas_read=[]
    alarm=""
    try:
        # Connect to the slave
        master = modbus_tcp.TcpMaster()
        master.set_timeout(5.0)
        logging.info("connected")

        # rerutn sensordata modified 220903
        datas_read=master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10)

        logging.info(datas_read)


        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 2, data_format='f'))

        # Read and write floats
        # master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, starting_address=0, output_value=[3.14], data_format='>f')
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 2, data_format='>f'))

        # send some queries
        # logger.info(master.execute(1, cst.READ_COILS, 0, 10))
        # logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
        # logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
        # logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
        # logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 100, output_value=54))
        # logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
        # logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))

    except modbus_tk.modbus.ModbusError as exc:
        logging.info("%s- Code=%d", exc, exc.get_exception_code())

    return datas_read

if __name__ == "__main__":
    main()
import threading


# class MyThread(threading.Thread):
#     def __init__(self, func):
#         '''
#         :param func: 可调用的对象
#         :param args: 可调用对象的参数
#         '''
#         threading.Thread.__init__(self)
#         self.func = func
#         # self.args = args
#
#     def run(self):
#         self.func(self)
#coding:utf-8
import logging
import colorlog
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter


class Journal(object):

    def __init__(self,name):
        self.name = name
        # self.content = None

    def SAVE_LOG(self):
        fmt = "%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s"
        # LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(filename='./log/log.txt', level=logging.DEBUG, format=fmt)
    
    
    def SAVE_INFO(self,content):
        self.SAVE_LOG()
        logging.info(content)

    def INFO(self,content):
        """
        s = Journal('Fuzz_WaF','hello word')
        s.INFO()

        >>> Tue, 23 Apr 2019 10:40:53  log.py  INFO [line:41] INFO hello word
        """
        fmt = "%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s"
        logging.basicConfig(filename='./log/log.txt', level=logging.INFO, format=fmt)
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s  %(log_color)s%(funcName)s [line:%(log_color)s%(lineno)d] %(log_color)s%(levelname)s %(log_color)s%(message)s"
        datefmt = '%a, %d %b %Y %H:%M:%S'

        formatter = ColoredFormatter(fmt=fmt,
                            datefmt=datefmt,
                            reset=True,
                            secondary_log_colors={},
                            style='%'
                            )

        hd_1 = logging.StreamHandler()
        hd_1.setFormatter(formatter)
        logger.addHandler(hd_1)
        logger.info(content)

    def SAVE_WARNING(self,content):
        self.SAVE_LOG()
        logging.warning(content)

    def WARNING(self,content):
        fmt = "%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s"
        logging.basicConfig(filename='./log/log.txt', level=logging.WARNING, format=fmt)
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.WARNING)
        fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s  %(log_color)s%(funcName)s [line:%(log_color)s%(lineno)d] %(log_color)s%(levelname)s %(log_color)s%(message)s"
        datefmt = '%a, %d %b %Y %H:%M:%S'

        formatter = ColoredFormatter(fmt=fmt,
                            datefmt=datefmt,
                            reset=True,
                            secondary_log_colors={},
                            style='%'
                            )

        hd_1 = logging.StreamHandler()
        hd_1.setFormatter(formatter)
        logger.addHandler(hd_1)
        logger.warning(content)

    def SAVE_ERROR(self,content):
        self.SAVE_LOG()
        logging.error(content)

    def ERROR(self,content):
        fmt = "%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s"
        logging.basicConfig(filename='./log/log.txt', level=logging.ERROR, format=fmt)
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.ERROR)
        fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s  %(log_color)s%(funcName)s [line:%(log_color)s%(lineno)d] %(log_color)s%(levelname)s %(log_color)s%(message)s"
        datefmt = '%a, %d %b %Y %H:%M:%S'

        formatter = ColoredFormatter(fmt=fmt,
                            datefmt=datefmt,
                            reset=True,
                            secondary_log_colors={},
                            style='%'
                            )

        hd_1 = logging.StreamHandler()
        hd_1.setFormatter(formatter)
        logger.addHandler(hd_1)
        logger.error(content)

    def SAVE_CRITICAL(self,content):
        self.SAVE_LOG()
        logging.critical(content)

    def CRITICAL(self,content):
        fmt = "%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s"
        logging.basicConfig(filename='./log/log.txt', level=logging.CRITICAL, format=fmt)
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.CRITICAL)
        fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s  %(log_color)s%(funcName)s [line:%(log_color)s%(lineno)d] %(log_color)s%(levelname)s %(log_color)s%(message)s"
        datefmt = '%a, %d %b %Y %H:%M:%S'

        formatter = ColoredFormatter(fmt=fmt,
                            datefmt=datefmt,
                            reset=True,
                            secondary_log_colors={},
                            style='%'
                            )

        hd_1 = logging.StreamHandler()
        hd_1.setFormatter(formatter)
        logger.addHandler(hd_1)
        logger.critical(content)

    def SAVE_DEBUG(self,content):
        self.SAVE_LOG()
        logging.debug(content)

    def DEBUG(self,content):
        fmt = "%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s"
        logging.basicConfig(filename='./log/log.txt', level=logging.DEBUG, format=fmt)
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)
        fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s  %(log_color)s%(funcName)s [line:%(log_color)s%(lineno)d] %(log_color)s%(levelname)s %(log_color)s%(message)s"
        datefmt = '%a, %d %b %Y %H:%M:%S'

        formatter = ColoredFormatter(fmt=fmt,
                            datefmt=datefmt,
                            reset=True,
                            secondary_log_colors={},
                            style='%'
                            )

        hd_1 = logging.StreamHandler()
        hd_1.setFormatter(formatter)
        logger.addHandler(hd_1)
        logger.debug(content)

    


# def test():
#     import logging
#     from logging.handlers import RotatingFileHandler
#     from colorlog import ColoredFormatter
#     from logging import basicConfig

#     #第一步：创建一个日志收集器logger(任务创建)
#     logger = logging.getLogger("autotest")

#     #第二步：修改日志的输出级别(输出级别)
#     logger.setLevel(logging.DEBUG)

#     #第三步：设置输出的日志内容格式(输出格式)
#     fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s  %(log_color)s%(funcName)s [line:%(log_color)s%(lineno)d] %(log_color)s%(levelname)s %(log_color)s%(message)s"
#     LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
#     datefmt = '%a, %d %b %Y %H:%M:%S'

#     formatter = ColoredFormatter(fmt=fmt,
#                            datefmt=datefmt,
#                            reset=True,
#                            secondary_log_colors={},
#                            style='%'
#                            )

#     basicConfig(
#                 filename='./log/log.txt',
#                 level=logging.debug,
#                 format=LOG_FORMAT
#     )

#     #设置输出渠道--输出到控制台(输出渠道)
#     hd_1 = logging.StreamHandler()
#     #在handler上指定日志内容格式(内容格式)
#     hd_1.setFormatter(formatter)


#     #第五步：将headler添加到日志logger上(添加)
#     logger.addHandler(hd_1)
#     s = {1,2,3,4,5,6,7}
#     #第六步：调用输出方法(调用)
#     logger.debug("我是debug级别的日志")
#     logger.info("我是info级别的日志")
#     logger.warning("我是warning级别的日志")
#     logger.warning(s)
#     logger.critical("我的critical级别的日志")
#     logger.error("我是error级别的日志输出")

# test()









# s = Journal('Fuzz_WaF','hello word')
# s.SAVE_INFO()
# s.SAVE_ERROR()
# s.INFO()

































# logger = logging.getLogger("autotest")
# logger = logging.getLogger("Fuzz_WaF")
# logger.setLevel(logging.INFO)
# fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s  %(log_color)s%(funcName)s [line:%(log_color)s%(lineno)d] %(log_color)s%(levelname)s %(log_color)s%(message)s"
# datefmt = '%a, %d %b %Y %H:%M:%S'

# formatter = ColoredFormatter(fmt=fmt,
#                        datefmt=datefmt,
#                        reset=True,
#                        secondary_log_colors={},
#                        style='%'
#                        )

# hd_1 = logging.StreamHandler()
# hd_1.setFormatter(formatter)
# logger.addHandler(hd_1)
# logger.info("我是info级别的日志")















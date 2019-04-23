import logging
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter

#第一步：创建一个日志收集器logger(任务创建)
logger = logging.getLogger("autotest")

#第二步：修改日志的输出级别(输出级别)
logger.setLevel(logging.DEBUG)

#第三步：设置输出的日志内容格式(输出格式)
fmt = "%(log_color)s%(asctime)s  %(log_color)s%(filename)s  %(log_color)s%(funcName)s [line:%(log_color)s%(lineno)d] %(log_color)s%(levelname)s %(log_color)s%(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

formatter = ColoredFormatter(fmt=fmt,
                       datefmt=datefmt,
                       reset=True,
                       secondary_log_colors={},
                       style='%'
                       )

logging.basicConfig(level=logging.warning,
                    filename='./log/log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

#设置输出渠道--输出到控制台(输出渠道)
hd_1 = logging.StreamHandler()
#在handler上指定日志内容格式(内容格式)
hd_1.setFormatter(formatter)


#第五步：将headler添加到日志logger上(添加)
logger.addHandler(hd_1)
s = {1,2,3,4,5,6,7}
#第六步：调用输出方法(调用)
logger.debug("我是debug级别的日志")
logger.info("我是info级别的日志")
logger.warning("我是warning级别的日志")
logger.warning(s)
logger.critical("我的critical级别的日志")
logger.error("我是error级别的日志输出")





# # coding=utf-8
# __author__ = 'liu.chunming'
# import logging
 
# logging.basicConfig(level=logging.WARNING,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# # use logging
# logging.info('this is a loggging info message')
# logging.debug('this is a loggging debug message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')








# # coding=utf-8
# __author__ = 'liu.chunming'
# import logging
 
# logging.basicConfig(level=logging.WARNING,
#                     filename='./log/log.txt',
#                     filemode='w',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# # use logging
# logging.info('this is a loggging info message')
# logging.debug('this is a loggging debug message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')


# # coding=utf-8
# __author__ = 'liu.chunming'
# import logging
 
# # 第一步，创建一个logger
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)    # Log等级总开关
 
# # 第二步，创建一个handler，用于写入日志文件
# logfile = './log/logger.txt'
# fh = logging.FileHandler(logfile, mode='w')
# fh.setLevel(logging.DEBUG)   # 输出到file的log等级的开关
 
# # 第三步，再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关
 
# # 第四步，定义handler的输出格式
# formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
 
# # 第五步，将logger添加到handler里面
# logger.addHandler(fh)
# logger.addHandler(ch)
 
# # 日志
# logger.debug('this is a logger debug message')
# logger.info('this is a logger info message')
# logger.warning('this is a logger warning message')
# logger.error('this is a logger error message')
# logger.critical('this is a logger critical message')
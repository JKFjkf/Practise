import logging
import datetime

#获取日志记录器，配置日至等级

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

#默认日志格式
formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
#输出到控制台的handler
chlr = logging.StreamHandler
#配置默认日志格式
chlr.setFormatter(formatter)


#日志记录器增加此handler
logger.addHandler(chlr)

def log(func):

    def inner(*args,**kwargs):
        timestamp = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        res = func(*args,**kwargs)
        logger.debug(f"func:{func.__name__} {args} -> {res}")
        return res
    return inner()




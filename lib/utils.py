import logging
from config import config

def getlogger(path=config.LOGPATH_SPYDER, level=logging.DEBUG):
    # levels - debug, info, warn, error, critical
    # sample: Mon, 05 Dec 2022 23:13:42 root INFO:some info. Default: 2022-12-05 23:18:21,836 root INFO:some info
    # datefmt='%a, %d %b %Y %H:%M:%S' => Mon, 05 Dec 2022 23:13:42. Default: 2022-12-05 23:18:21
    logging.basicConfig(filename=path, filemode='w',
                        format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S', level=level)
    logger = logging.getLogger()
    return logger

def crypt(to_encrypt):
    chars = [c for c in to_encrypt]
    keyy = []
    for c in chars:
        keyy.append(str(ord(c)))
    return ''.join(keyy)

if __name__ == "__main__":
    lgr = getlogger()    # can pass __name__
    lgr.debug("lgr debug")
    lgr.info("lgr info")
    lgr.error("ee", exc_info=True)  #traceback
    lgr.critical("red alert")

# REFERENCES
# https://dotnettutorials.net/lesson/customized-logging-in-python/
# https://docs.python.org/3/library/logging.html
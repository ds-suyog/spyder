
import os
BASEDIR = os.getcwd()    #verify dynamic setting of CWD

BASE_URL = "https://www.bseindia.com/"
URL_GAINER = "https://www.bseindia.com/markets/equity/EQReports/mktwatchR.html?filter=gainer*all$all$"
URL_LOOSER = "https://www.bseindia.com/markets/equity/EQReports/mktwatchR.html?filter=loser*all$all$"

LOGPATH_SPYDER = "{}/logs/spyder.log".format(BASEDIR)
LOGPATH_GECKO = "{}/logs/gecko.log".format(BASEDIR)
GECKODRIVER_BIN = '{}/bin/geckodriver'.format(BASEDIR)

CRAWLED_TRENDING = "tmp/crawled/trending.html"
CRAWLED_GAINER = "tmp/crawled/gainer.html"
CRAWLED_LOOSER = "tmp/crawled/looser.html"

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

BSE_DB = 'bse'
REPORT_BSE_FPATH = '{}/reports/report_bse.txt'.format(BASEDIR)
REPORT_BSE_FNAME = 'report_bse.txt'
REPORT_KEYS_FPATH = '{}/reports/report_keys.txt'.format(BASEDIR)
REPORT_KEYS_FNAME = 'report_keystats.txt'

# geckodriver: geckodriver-v0.32.0-linux64.tar
# Author: Suyog K. Sethia <suyog.sethia@gmail.com>.

"""Parser parses data from crawled htmls.
This module is responsible for:
    - parsing
    - making call to db_ops for storing data
"""

__version__ = '1.1'

from config import *
import utils
import os
import sys; sys.path.append(BASEDIR)
from bs4 import BeautifulSoup
import json
from db_ops import MongoOps
from db_ops import ElasticSearchOps

MODE = None

# to-do: add timestamp too, to keep track of top gainers
# to do: close mongo and elastic search clients if required.

class Parser:
    """

    """
    def __init__(self):
        self.logger = utils.getlogger()
        self.mongo_ops = MongoOps()
        self.es_ops = ElasticSearchOps()

    def parse(self):
        self.logger.debug("\n\n=======	parsing Trending")
        with open (CRAWLED_TRENDING, 'r', encoding="utf8") as f:
            soup = BeautifulSoup(f, "html.parser")
        div_u2d1 = soup.find_all('div', id='u2_d1')
        trending = [{'_id': utils.crypt(anc.text), 'name': anc.text} for rank, anc in enumerate(div_u2d1[0].find_all('a'))]
        self.mongo_ops.insert_one(trending, 'trending')
        self.es_ops.bulk_insert(trending, 'bse_trending', 'trending')
        # os.remove(CRAWLED_TRENDING)

        self.logger.debug("parsing Gainers")
        headers = []    # ['Security', 'LTP (₹)', 'Change', '% Ch.']
        gainers = []
        top_gainer_names = []
        with open(CRAWLED_GAINER) as f:  #open( ,encoding="utf8")
            soup = BeautifulSoup(f, "html.parser")
        div = soup.find('div', id="gain")
        tbodys = div.findAll('tbody')
        trs = tbodys[0].findAll('tr')
        for td in trs[0]:
            if td != '\n':
                headers.append(td.strong.text)
        for tbody in tbodys[1:-1]:
            document = []
            trs = tbody.findAll('tr')
            for td in trs[0]:
                if td != '\n':
                    document.append(td.text)
            top_gainer_names.append(document[0])
            gainers.append(dict(zip(headers, document)))

        lst_g = ["%s.%s"%(i+1,v) for i,v in enumerate(top_gainer_names)]
        self.mongo_ops.insert_one(gainers, 'gainers')
        self.es_ops.bulk_insert(gainers, 'bse_gainers', 'gainers')
        # os.remove(CRAWLED_GAINER)

        self.logger.debug("parsing loosers")
        headers = []    # ['Security', 'LTP (₹)', 'Change', '% Ch.']
        loosers = []
        top_looser_names = []
        with open(CRAWLED_LOOSER) as f:  #open( ,encoding="utf8")
            soup = BeautifulSoup(f, "html.parser")
        # import pdb; pdb.set_trace()
        div = soup.find('div', id="lose")
        tbodys = div.findAll('tbody')
        trs = tbodys[0].findAll('tr')
        for td in trs[0]:
            if td != '\n':
                headers.append(td.strong.text)
        for tbody in tbodys[1:-1]:
            document = []
            trs = tbody.findAll('tr')
            for td in trs[0]:
                if td != '\n':
                    document.append(td.text)
            top_looser_names.append(document[0])
            loosers.append(dict(zip(headers, document)))

        lst_g = ["%s.%s"%(i+1,v) for i,v in enumerate(top_gainer_names)]
        self.mongo_ops.insert_one(loosers, 'loosers')
        self.es_ops.bulk_insert(loosers, 'bse_loosers', 'loosers')
        # os.remove(CRAWLED_LOOSER)

        # self.logger.info("parsing completed!!")

def main():
    parser = Parser()
    try:
        parser.parse()
    except Exception as e:
        parser.logger("error: {}".format(e), exc_info=True)
    finally:
        pass

if __name__ == '__main__':
    main()



# Author: Suyog K. Sethia <suyog.sethia@gmail.com>.

"""Spyder crawls web and downloads target webpages.
This module is responsible for:
    - crawling
    - storing crawled pages in the form of html
"""

__version__ = '1.1'
from config.config import *
import lib.utils as utils
import sys; sys.path.append(BASEDIR)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

MODE = None

class SpyderBot:
    """

    """
    def __init__(self):
        self.logger = utils.getlogger()
        # pass browser/agent info and proxy later
        self.driver = webdriver.Firefox(executable_path=r"{}".format(GECKODRIVER_BIN), log_path='{}'.format(LOGPATH_GECKO))

    def crawl(self):
        """Launch crawl process
        The instance method performs data acquisition.
        :param None
        :return None.
        """

        self.logger.debug("\n\n================================= Spyder started crawling. ")
        # driver.maximize_window()
        # time.sleep(2)
        page = self.driver.get(BASE_URL)
        time.sleep(2)

        # import pdb; pdb.set_trace()
        # driver.implicitly_wait(2)
        # link = driver.find_element("link text", "Trending")
        # link.click()
        # For improved reliability, consider using WebDriverWait in combination with element_to_be_clickable.
        xpath_trending = "// *[ @ id = 'skipcontent'] / div[1] / div / div[2] / div / div / ul / li[5] / a"
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_trending)))
        element.click()
        # elem = driver.find_element(By.XPATH, xpath_trending)
        # elem.get_attribute('href')
        # import pdb; pdb.set_trace()
        html_source = self.driver.page_source
        with open (CRAWLED_TRENDING, 'w') as f:
            f.write(html_source)

        xpath_gainer = "//*[@id='gainer']"
        xpath_gainer_full = "//*[@id='gain']/table/tbody[7]/tr/td/a/i"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_gainer))).click()
        print(" ==== == == === == ==== gainer")
        # import pdb; pdb.set_trace()
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_gainer_full))).click()
        # Error: selenium.common.exceptions.ElementNotInteractableException: Message: Element <i class="fa fa-arrow-circle-right"> could not be scrolled into view. Stacktrace:
        print(" ==== == == === == ==== gainer full")
        # import pdb; pdb.set_trace()
        html_source = self.driver.page_source
        with open(CRAWLED_GAINER, 'w') as f:
            f.write(html_source)

        xpath_looser = "//*[@id='loser']"
        xpath_looser_full = "//*[@id='lose']/table/tbody[7]/tr/td/a/i"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_looser))).click()
        print(" ==== == == === == ==== looser")
        # import pdb; pdb.set_trace()
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_looser_full))).click()
        print(" ==== == == === == ==== losser full")
        # import pdb; pdb.set_trace()
        html_source = self.driver.page_source
        with open(CRAWLED_LOOSER, 'w') as f:
            f.write(html_source)

        # params_l = {'GLtype':	'loser', 'IndxGrp':	'AllMkt', 'IndxGrpval':	'AllMkt', 'orderby':	'all'}
        # page_l = requests.get(url = URL_LOOSER, params = params_l,)
        # page_l.raise_for_status()
        # with open("tmp/content_looser.html", 'w') as f:
        # 	f.write(page_l.text)
        self.logger.info("crawling completed!")
        # import pdb; pdb.set_trace()
def main():
    spyder = SpyderBot()
    try:
        spyder.crawl()
    except Exception as e:
        spyder.logger("error: {}".format(e), exc_info=True)
    finally:
        spyder.driver.close()
        #TO-DO# close mongo and es client too. check how to close

if __name__ == '__main__':
    main()



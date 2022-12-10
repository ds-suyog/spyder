from config.config import *
from lib import utils
# import sys; sys.path.append("{}/lib".format(BASEDIR))
from lib import spyder
from lib import parser
from lib import reportbse
from lib import keys_stats as ks

CRAWL = [False, True][0]
PARSE = [False, True][0]
GENERATE_REPORTS = [False, True][1]

def trigger_workflow():
    logger = utils.getlogger()
    logger.debug("\n\n==============================================================  Triggering Spyder")
    if CRAWL == True:
        spyder.main()
    if PARSE == True:
        parser.main()
    if GENERATE_REPORTS == True:
        reportbse.main()
        ks.main()

def check_job_queue():
      pass
#     logger = constant.getlogger()
#     logger.debug("\n\n==============================================================  CHECKING Redis")
#     #Implementing redis queue functionality
#     from rq import use_connection, Queue
#     use_connection()
#     webscr = Queue('bse_webscrap')
#     webscr.enqueue(worker_bse_report.Worker().run,
#                args=(sender_name, sender_email, email_subject, body),
#                kwargs={}, )
#     key_stats = Queue('keys_stats')
#     key_stats.enqueue(worker_keys_stats.Worker().run,
#         args = (sender_name, sender_email, email_subject, body),
#         kwargs = {},)

def main():
    # check_job_queue() for job
    trigger_workflow()


if __name__ == '__main__':
    main()
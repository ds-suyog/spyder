from config import *
import utils
import sys; sys.path.append("{}/utils".format(BASEDIR))
import reportbse
import keys_stats as ks
import spyder
import parser

def trigger_spyder():
    logger = utils.getlogger()
    logger.debug("\n\n==============================================================  Triggering Spyder")
    # import pdb; pdb.set_trace()
    # spyder.main()
    # reportbse.main()
    # report_filename = ks.main(dbname)

# def check_redis_queue():
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
    trigger_spyder()
    # check_redis_queue()

if __name__ == '__main__':
    main()
import schedule
import time
import logging

logger = logging.getLogger(__name__)


record = {'name': 'Ashik', 'age': 25, 'city': 'Dhaka'}

def job():
    def filter_record(item):
        return item[1] >= 20

    filtered_dict = dict(filter(filter_record, record.items()))
    logger.info(filtered_dict['age'])
    
schedule.every().day.at("15:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

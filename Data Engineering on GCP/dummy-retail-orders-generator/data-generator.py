import logging
import logging.handlers as handlers
import time
from threading import Thread
#import utils
import order_utils as order_utils
import customer_utils as customer_utils

logger = logging.getLogger('retail-customer-generator')

logger.setLevel(logging.INFO)

## Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  
def get_logger():
	
	logHandler = handlers.TimedRotatingFileHandler(r"logs/data-generator.log", when='H', interval=1, backupCount=0)
	logHandler.setLevel(logging.INFO)
	logHandler.setFormatter(formatter)

	errorLogHandler = handlers.RotatingFileHandler(r"logs/data-generator_error.log", maxBytes=5000, backupCount=0)
	errorLogHandler.setLevel(logging.ERROR)
	errorLogHandler.setFormatter(formatter)
	logger.addHandler(logHandler)
	logger.addHandler(errorLogHandler)
	return logger
         
def main():
	print("Process started..........")
	get_logger()
	while (1):
		customer_utils._generate_new_customers(logger);time.sleep(60)
		order_utils._place_new_orders(logger);time.sleep(30)
		order_utils._place_new_orders(logger);time.sleep(10)		
     
main()

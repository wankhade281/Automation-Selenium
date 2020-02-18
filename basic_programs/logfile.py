import logging

logging.basicConfig(filename="/basic_programs/log_details.txt",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m-%d-%Y %I:%M:%S %p', level=logging.DEBUG)

logging.debug("This is debug message")
logging.info("This is logging message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
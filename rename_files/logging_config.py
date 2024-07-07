import logging

def setup_logging(): #Sets the format for log messages to include the timestamp, log level, and message.
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

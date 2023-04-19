# import necessary libraries
import logging as log
from pathlib import Path

def start_logging():
    filename = Path('./machina.log')
    log.basicConfig(
        level=log.DEBUG,
        format="%(asctime)s : %(levelname)s : %(filename)s[%(lineno)d] : %(message)s",
        filename=filename,
        filemode='w'
    )
    log.info("Logging Started")
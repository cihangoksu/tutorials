# %% Logging module test
print('Hello')
import logging
logger = logging.getLogger('my logger')

handler = logging.FileHandler('mylog.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.setLevel(logging.DEBUG)
logger.debug('This is a debug message')
logger.info('This is an info message')


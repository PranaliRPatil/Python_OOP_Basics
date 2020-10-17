''' https://docs.python.org/3/howto/logging.html
Loggin standard levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
Default level: WARNING (can change by passing level param to logging.basicConfig())

'''

import logging
# default date format is ISO8601 or RFC 3339 #2010-12-12 11:41:42,612
logging.basicConfig(format='%(asctime)s:%(levelname)s %(message)s', level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('You are debugging.')
logging.info('This is just for Info.')
logging.warning('This is for warning.')
logging.error('This is an Error.')
logging.critical('It too critical to even run it..')

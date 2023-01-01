# --------------------------------------------------------------------------------------------------
# Logging: add a logging file to code
#   - prints out to console or file
#   - helps to trace the code execution
#   - logging level: DEBUG / INFO / WARNING / ERROR / CRITICAL
#   - name: logging module gives it to the default logger, [default] 'root'
#
#   Basic Config:
#       filename:   file name and extension
#       mode:       file mode (w/a)
#       format:     format of the log message
#       level:      level of severity
#
#   getLogger returns a logger with the specified name
# --------------------------------------------------------------------------------------------------

import os
import logging          # logging module
os.system('cls')        # cls command

print(dir(logging))

logging.basicConfig(filename= 'my_log.log', 
                    filemode= 'a', 
                    format= '%(asctime)s:\t %(name)s | %(levelname)s | \'%(message)s\'',
                    datefmt= '%d/%m/%Y, %H:%M:%S')

my_logger = logging.getLogger('Amr')

my_logger.critical('This is a critical status')
my_logger.error('This is an error message')
my_logger.warning('This is warning')
my_logger.info('This is an info')
my_logger.debug('This is debug')

my_logger2 = logging.getLogger('Lina')

my_logger2.critical('This is a critical status')
my_logger2.error('This is an error message')
my_logger2.warning('This is warning')
my_logger2.info('This is an info')
my_logger2.debug('This is debug')

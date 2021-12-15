# [로깅 HOWTO — Python 3.10.1 문서](https://docs.python.org/ko/3/howto/logging.html)
# [로깅 요리책 — Python 3.10.1 문서](https://docs.python.org/ko/3/howto/logging-cookbook.html#logging-cookbook)
import glob
import logging
import logging.handlers
import time

# rotating
LOG_FILE_NAME = "./my_example_code/howto_logging/logging_rotating_file_example.log"
my_logger = logging.getLogger("my.logger")
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(
    LOG_FILE_NAME, maxBytes=20, backupCount=3
)

my_logger.addHandler(handler)

for i in range(20):
    my_logger.debug("i = %d" % i)


log_files = glob.glob("%s*" % LOG_FILE_NAME)

for file_name in log_files:
    print(file_name)


# TimeRotating
LOG_FILE_NAME = "./my_example_code/howto_logging/logging_time_file_example.log"
time_logger = logging.getLogger("my.time_logger")
time_logger.setLevel(logging.DEBUG)

handler = logging.handlers.TimedRotatingFileHandler(
    LOG_FILE_NAME, when="S", interval=1, backupCount=3
)

time_logger.addHandler(handler)

for i in range(5):
    time_logger.debug("i = %d" % i)
    time.sleep(1)


log_files = glob.glob("%s*" % LOG_FILE_NAME)

for file_name in log_files:
    print(file_name)

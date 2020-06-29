import logging
import logging.config
import logger_test  # this is an external module

# load the logging configuration
logging.config.fileConfig('log.conf', disable_existing_loggers=False)
log = logging.getLogger(__name__)

# calling external module
logger_test.foo()
bar = logger_test.Bar()
bar.bar()

log.debug("This is a debug log")
log.info("This is an info log")
log.warning("This is a warning log")
log.error("This is an error log")
log.critical("This is a critical log")

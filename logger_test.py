import logging

log = logging.getLogger(__name__)

def foo():
    log.info('Hello from external module')

class Bar(object):
    def bar(self):
        log.error('Hello again from external module')

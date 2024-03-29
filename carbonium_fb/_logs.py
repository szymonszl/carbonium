"""This module configures logging for Carbonium"""
import logging
logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
log = logging.getLogger('carbonium')
log.setLevel(logging.DEBUG) # FIXME, should be defined at bot instantiation

_fblog = logging.getLogger('client')
_fblog.setLevel(logging.WARNING) # don't ask

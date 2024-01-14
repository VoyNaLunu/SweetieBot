import logging
import sys

logger = logging
logger.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s: %(message)s')

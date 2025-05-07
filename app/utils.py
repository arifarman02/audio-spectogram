import logging


# Logger
logger = logging.getLogger('spectogram')

logger.setLevel(logging.INFO)

handler = logging.StreamHandler()

format = '%(asctime)s - %(levelname)s - %(filename)s - %(message)s'
formatter = logging.Formatter(format)
handler.setFormatter(formatter)

logger.addHandler(handler)
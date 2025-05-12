import logging
from pyrr import Matrix44


# Logger
logger = logging.getLogger('spectogram')

logger.setLevel(logging.INFO)

handler = logging.StreamHandler()

format = '%(asctime)s - %(levelname)s - %(filename)s - %(message)s'
formatter = logging.Formatter(format)
handler.setFormatter(formatter)

logger.addHandler(handler)



def orthographic(w, h):
    return Matrix44.orthogonal_projection(
        0, w, h, 0, 1, -1, dtype='f4')
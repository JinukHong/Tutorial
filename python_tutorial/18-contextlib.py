import time
import logging
from contextlib import contextmanager

# with 구문을 만드는

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)

def func1():
    # 기본은 info로 설정되어 있음, 젤 낮은 레벨.
    logging.debug("with 외부")
    with debug_logging(logging.DEBUG): # 자동으로 해야할 일을 with 로 구현.
        logging.debug("with 내부")
        
    
if __name__ == "__main__":
    func1()
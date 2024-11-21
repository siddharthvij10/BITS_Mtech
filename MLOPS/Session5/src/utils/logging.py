import sys
from pathlib import Path
from loguru import logger
import functools

def setup_logger(log_dir=None):
    if log_dir:
        log_file = Path(log_dir)
    else:
        log_file = Path("logs/train.log")
    
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger.remove()
    logger.add(sys.stderr, level="INFO")
    logger.add(log_file, rotation="10 MB", level="DEBUG")

    return logger

def task_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Finished {func.__name__}")
            return result
        except Exception as e:
            logger.exception(f"Exception in {func.__name__}: {str(e)}")
            raise
    return wrapper

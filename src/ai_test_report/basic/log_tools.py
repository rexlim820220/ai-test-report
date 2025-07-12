# src/ai_test_report/basic/log_tools.py
import logging

def setup_logger(name="ai_test_report", level=logging.INFO):
    """
    Set up and return a logger instance with consistent format.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.setLevel(level)
        logger.addHandler(stream_handler)
    return logger

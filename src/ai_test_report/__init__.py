import logging
import os
import yaml
from .basic.common_tools import summarize_results
from .basic.log_tools import setup_logger

__all__ = ["summarize_results", "setup_logger"]

config_path = os.path.join(os.path.dirname(__file__), "config.yml")

try:
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    config = {}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai_test_report")
logger.info("ai_test_report initialized.")

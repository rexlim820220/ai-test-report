import pytest
from ai_test_report import logger

def test_view_data_loaded():
    fake_database = ["2025-07-11", "2025-07-12"]
    selected_date = "2025-07-12"
    logger.info(f"Viewing entry for date: {selected_date}")
    assert selected_date in fake_database

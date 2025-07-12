import pytest
from ai_test_report import logger

def test_login_success():
    username = "test"
    password = "123"
    logger.info(f"Trying login with username={username} and password={password}")
    assert username == "test" and password == "123"

def test_login_failure():
    username = ""
    password = ""
    logger.info("Trying login with empty credentials")
    assert username != "test" or password != "123"

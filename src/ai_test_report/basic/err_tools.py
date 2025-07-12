# src/ai_test_report/basic/err_tools.py

import traceback

def format_exception_summary(exc: Exception) -> str:
    """
    Returns a one-line summary of an exception.
    """
    return f"{type(exc).__name__}: {str(exc)}"

def format_full_trace(exc: Exception) -> str:
    """
    Returns the full traceback string of an exception.
    """
    return "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))

def safe_execute(func, *args, **kwargs):
    """
    Executes a function and catches/logs any errors.
    Returns (result, error) tuple.
    """
    try:
        result = func(*args, **kwargs)
        return result, None
    except Exception as e:
        return None, format_exception_summary(e)

"""
Configuration module for OrangeHRM automation framework
"""
from playwright.config import (
    BASE_URL,
    USERNAME,
    PASSWORD,
    BROWSER,
    HEADLESS,
    TIMEOUT,
    NAVIGATION_TIMEOUT,
    SCREENSHOT_DIR,
    TEST_DATA
)

__all__ = [
    "BASE_URL",
    "USERNAME",
    "PASSWORD",
    "BROWSER",
    "HEADLESS",
    "TIMEOUT",
    "NAVIGATION_TIMEOUT",
    "SCREENSHOT_DIR",
    "TEST_DATA"
]


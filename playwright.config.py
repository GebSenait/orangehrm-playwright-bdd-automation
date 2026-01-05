"""
Playwright configuration for OrangeHRM automation framework
"""
from playwright.sync_api import Playwright, sync_playwright
import os

# Base URL for OrangeHRM
BASE_URL = "https://opensource-demo.orangehrmlive.com"

# Credentials
USERNAME = "Admin"
PASSWORD = "admin123"

# Browser settings
BROWSER = "chromium"  # Options: chromium, firefox, webkit
HEADLESS = True
SLOW_MO = 0  # milliseconds

# Timeout settings
TIMEOUT = 30000  # 30 seconds
NAVIGATION_TIMEOUT = 60000  # 60 seconds

# Screenshot settings
SCREENSHOT_ON_FAILURE = True
SCREENSHOT_DIR = "screenshots"

# Test data
TEST_DATA = {
    "valid_employee_name": "John",
    "invalid_employee_name": "NonExistentEmployee123",
    "report_name": "Employee Report",
}


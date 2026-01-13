"""
Playwright configuration for OrangeHRM automation framework
"""

# Base URL for OrangeHRM
BASE_URL = "https://opensource-demo.orangehrmlive.com"

# Credentials
USERNAME = "Admin"
PASSWORD = "admin123"

# Browser settings
BROWSER = "chromium"  # Options: chromium, firefox, webkit
# Detect CI environment (GitHub Actions, GitLab CI, etc.)
import os
HEADLESS = os.getenv("CI", "false").lower() in ("true", "1")  # True in CI, False locally
SLOW_MO = 0 if HEADLESS else 500  # No slow-mo in CI, 500ms locally for debugging

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


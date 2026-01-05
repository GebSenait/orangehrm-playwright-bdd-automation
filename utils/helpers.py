"""
Helper utilities for OrangeHRM automation framework
"""
import os
from datetime import datetime
from pathlib import Path
from playwright.sync_api import Page
from utils.config import SCREENSHOT_DIR


def ensure_screenshot_dir():
    """Ensure screenshot directory exists"""
    Path(SCREENSHOT_DIR).mkdir(parents=True, exist_ok=True)


def capture_screenshot(page: Page, scenario_name: str):
    """
    Capture screenshot on test failure
    
    Args:
        page: Playwright page object
        scenario_name: Name of the test scenario
    """
    ensure_screenshot_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = scenario_name.replace(" ", "_").replace("/", "_")
    filename = f"{SCREENSHOT_DIR}/{safe_name}_{timestamp}.png"
    page.screenshot(path=filename, full_page=True)
    return filename


def wait_for_element_visible(page: Page, selector: str, timeout: int = 30000):
    """
    Wait for element to be visible
    
    Args:
        page: Playwright page object
        selector: CSS selector or locator
        timeout: Maximum wait time in milliseconds
    """
    page.wait_for_selector(selector, state="visible", timeout=timeout)


def wait_for_element_hidden(page: Page, selector: str, timeout: int = 30000):
    """
    Wait for element to be hidden
    
    Args:
        page: Playwright page object
        selector: CSS selector or locator
        timeout: Maximum wait time in milliseconds
    """
    page.wait_for_selector(selector, state="hidden", timeout=timeout)


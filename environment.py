"""
Behave environment configuration for OrangeHRM automation
"""
from behave import use_step_matcher
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS
from utils.helpers import capture_screenshot

use_step_matcher("parse")


def before_all(context):
    """Initialize browser before all scenarios"""
    context.playwright = sync_playwright().start()
    # Browser launch options optimized for CI
    launch_options = {
        "headless": HEADLESS,
        "args": [
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            "--disable-accelerated-2d-canvas",
            "--disable-gpu",
        ]
    }
    context.browser = context.playwright.chromium.launch(**launch_options)
    context.context = context.browser.new_context()
    context.page = context.context.new_page()


def after_all(context):
    """Clean up browser after all scenarios"""
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()


def after_scenario(context, scenario):
    """Clean up after each scenario and capture screenshot on failure"""
    if scenario.status == "failed" and hasattr(context, 'page'):
        capture_screenshot(context.page, scenario.name)


def before_scenario(context, scenario):
    """Reset context before each scenario"""
    # Clear cookies and storage to ensure clean session state
    if hasattr(context, 'context'):
        try:
            context.context.clear_cookies()
            context.context.clear_permissions()
        except Exception:
            pass  # Continue even if clearing fails
    
    # Clear any page objects from previous scenario
    if hasattr(context, 'search_page'):
        delattr(context, 'search_page')
    if hasattr(context, 'reports_page'):
        delattr(context, 'reports_page')


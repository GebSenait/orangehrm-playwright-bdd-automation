"""
Common step definitions shared across features
These steps are used in Background sections and can be reused
"""
from behave import given
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


@given('I am logged into OrangeHRM')
def step_login_common(context):
    """
    Common login step - can be used across all features
    
    This step definition ensures the login step is discoverable
    and navigable from feature files.
    """
    login_page = LoginPage(context.page)
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    assert login_page.is_logged_in(), "Login failed"


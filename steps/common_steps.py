"""
Common step definitions shared across features
These steps are used in Background sections and can be reused

Navigation: Hover over "Given I am logged into OrangeHRM" in any feature file
and Ctrl+Click to navigate to this step definition.
"""
from behave import given  # type: ignore
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


@given('I am logged into OrangeHRM')
def step_login_common(context):
    """
    Common login step - can be used across all features
    
    Linked to: pages/login_page.py -> LoginPage.login()
    Used in: features/search.feature, features/reports.feature
    
    This step definition ensures the login step is discoverable
    and navigable from feature files.
    """
    login_page = LoginPage(context.page)
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    assert login_page.is_logged_in(), "Login failed"


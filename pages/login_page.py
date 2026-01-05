"""
Login Page Object Model for OrangeHRM
"""
from playwright.sync_api import Page
from utils.config import BASE_URL, USERNAME, PASSWORD
from utils.helpers import wait_for_element_visible


class LoginPage:
    """Page Object for OrangeHRM Login page"""
    
    def __init__(self, page: Page):
        self.page = page
        self.username_input = 'input[name="username"]'
        self.password_input = 'input[name="password"]'
        self.login_button = 'button[type="submit"]'
        self.dashboard_heading = 'h6.oxd-text--h6'
    
    def navigate(self):
        """Navigate to OrangeHRM login page"""
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
    
    def login(self, username: str = None, password: str = None):
        """
        Login to OrangeHRM
        
        Args:
            username: Username (defaults to config USERNAME)
            password: Password (defaults to config PASSWORD)
        """
        username = username or USERNAME
        password = password or PASSWORD
        
        wait_for_element_visible(self.page, self.username_input)
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        self.page.wait_for_load_state("networkidle")
    
    def is_logged_in(self) -> bool:
        """Check if user is logged in by verifying dashboard presence"""
        try:
            wait_for_element_visible(self.page, self.dashboard_heading, timeout=10000)
            return True
        except:
            return False


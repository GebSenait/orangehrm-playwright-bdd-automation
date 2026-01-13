"""
Login Page Object Model for OrangeHRM
"""
from playwright.sync_api import Page  # type: ignore
from utils.config import BASE_URL, USERNAME, PASSWORD
from utils.helpers import wait_for_element_visible


class LoginPage:
    """Page Object for OrangeHRM Login page"""
    
    def __init__(self, page: Page):
        self.page = page
        # More flexible selectors for OrangeHRM
        self.username_input = 'input[name="username"], input[placeholder*="Username"], input.oxd-input'
        self.password_input = 'input[name="password"], input[type="password"]'
        self.login_button = 'button[type="submit"], button:has-text("Login")'
        self.dashboard_heading = 'h6.oxd-text--h6, h6[class*="oxd-text"]'
    
    def navigate(self):
        """Navigate to OrangeHRM login page"""
        self.page.goto(BASE_URL, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle", timeout=60000)
    
    def login(self, username: str = None, password: str = None):
        """
        Login to OrangeHRM
        
        Args:
            username: Username (defaults to config USERNAME)
            password: Password (defaults to config PASSWORD)
        """
        username = username or USERNAME
        password = password or PASSWORD
        
        # Navigate to base URL first
        self.page.goto(BASE_URL, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle", timeout=60000)
        self.page.wait_for_timeout(2000)  # Give page time to render
        
        # Check if already logged in - if so, skip login process
        if self.is_logged_in():
            return  # Already logged in, no need to login again
        
        # Wait for page to be ready
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(2000)  # Give page time to render
        
        # Try to find username input with multiple strategies
        try:
            username_locator = self.page.locator('input[name="username"]').first
            if not username_locator.is_visible(timeout=5000):
                username_locator = self.page.locator('input[placeholder*="Username"]').first
            username_locator.wait_for(state="visible", timeout=10000)
            username_locator.fill(username)
        except Exception:
            # Fallback: try by class
            self.page.locator('input.oxd-input').first.fill(username)
        
        # Fill password
        try:
            password_locator = self.page.locator('input[name="password"]').first
            if not password_locator.is_visible(timeout=3000):
                password_locator = self.page.locator('input[type="password"]').first
            password_locator.wait_for(state="visible", timeout=10000)
            password_locator.fill(password)
        except Exception:
            # Fallback: try password input by type
            try:
                self.page.locator('input[type="password"]').first.wait_for(state="visible", timeout=10000)
                self.page.locator('input[type="password"]').first.fill(password)
            except Exception:
                # Last resort: use any password input
                self.page.fill('input[type="password"]', password)
        
        # Click login button
        try:
            login_btn = self.page.locator('button[type="submit"]').first
            if not login_btn.is_visible(timeout=2000):
                login_btn = self.page.locator('button:has-text("Login")').first
            login_btn.click()
        except Exception:
            self.page.locator('button[type="submit"]').first.click()
        
        self.page.wait_for_load_state("networkidle", timeout=60000)
    
    def is_logged_in(self) -> bool:
        """Check if user is logged in by verifying dashboard presence or absence of login form"""
        try:
            # Check if dashboard heading is visible (user is logged in)
            wait_for_element_visible(self.page, self.dashboard_heading, timeout=5000)
            return True
        except Exception:
            # Check if login form is visible (user is not logged in)
            try:
                login_form = self.page.locator('input[name="username"]').first
                if login_form.is_visible(timeout=3000):
                    return False
            except Exception:
                pass
            # If neither is clearly visible, check URL
            current_url = self.page.url
            if "dashboard" in current_url.lower() or "index" in current_url.lower():
                return True
            return False


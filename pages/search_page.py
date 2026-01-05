"""
Search Page Object Model for OrangeHRM Employee Search
"""
from playwright.sync_api import Page
from utils.helpers import wait_for_element_visible


class SearchPage:
    """Page Object for OrangeHRM Employee Search functionality"""
    
    def __init__(self, page: Page):
        self.page = page
        # Navigation
        self.pim_menu = 'a[href*="pim"]'
        self.employee_list_menu = 'a[href*="viewEmployeeList"]'
        
        # Search elements
        self.employee_name_input = 'input[placeholder*="Employee Name"]'
        self.search_button = 'button[type="submit"]'
        self.reset_button = 'button[type="reset"]'
        
        # Results
        self.search_results_table = 'div.oxd-table-body'
        self.no_records_found = 'span.oxd-text--span'
        self.employee_name_cell = 'div.oxd-table-cell:first-child'
        
        # Filters
        self.employment_status_dropdown = 'div:has-text("Employment Status")'
        self.job_title_dropdown = 'div:has-text("Job Title")'
    
    def navigate_to_employee_list(self):
        """Navigate to Employee List page"""
        wait_for_element_visible(self.page, self.pim_menu)
        self.page.click(self.pim_menu)
        wait_for_element_visible(self.page, self.employee_list_menu)
        self.page.click(self.employee_list_menu)
        self.page.wait_for_load_state("networkidle")
        wait_for_element_visible(self.page, self.employee_name_input)
    
    def search_by_employee_name(self, employee_name: str):
        """
        Search for employee by name
        
        Args:
            employee_name: Name of the employee to search
        """
        wait_for_element_visible(self.page, self.employee_name_input)
        self.page.fill(self.employee_name_input, employee_name)
        # Wait for autocomplete suggestions
        self.page.wait_for_timeout(1000)
        # Select first suggestion if available
        try:
            suggestion = self.page.locator('div.oxd-autocomplete-option').first
            if suggestion.is_visible(timeout=2000):
                suggestion.click()
        except:
            pass
        self.page.click(self.search_button)
        self.page.wait_for_load_state("networkidle")
    
    def search_with_invalid_name(self, invalid_name: str):
        """
        Search with invalid employee name
        
        Args:
            invalid_name: Invalid employee name
        """
        wait_for_element_visible(self.page, self.employee_name_input)
        self.page.fill(self.employee_name_input, invalid_name)
        self.page.wait_for_timeout(1000)
        self.page.click(self.search_button)
        self.page.wait_for_load_state("networkidle")
    
    def apply_employment_status_filter(self, status: str):
        """
        Apply employment status filter
        
        Args:
            status: Employment status (e.g., "Full-Time Permanent")
        """
        wait_for_element_visible(self.page, self.employment_status_dropdown)
        self.page.click(self.employment_status_dropdown)
        self.page.wait_for_timeout(500)
        # Select the status option
        status_option = self.page.locator(f'text="{status}"').first
        if status_option.is_visible(timeout=2000):
            status_option.click()
    
    def apply_job_title_filter(self, job_title: str):
        """
        Apply job title filter
        
        Args:
            job_title: Job title to filter by
        """
        wait_for_element_visible(self.page, self.job_title_dropdown)
        self.page.click(self.job_title_dropdown)
        self.page.wait_for_timeout(500)
        # Select the job title option
        job_option = self.page.locator(f'text="{job_title}"').first
        if job_option.is_visible(timeout=2000):
            job_option.click()
    
    def get_search_results_count(self) -> int:
        """Get the number of search results"""
        try:
            wait_for_element_visible(self.page, self.search_results_table, timeout=5000)
            rows = self.page.locator('div.oxd-table-row').count()
            return rows
        except:
            return 0
    
    def is_no_records_found(self) -> bool:
        """Check if 'No Records Found' message is displayed"""
        try:
            no_records = self.page.locator('span.oxd-text--span:has-text("No Records Found")')
            return no_records.is_visible(timeout=5000)
        except:
            return False
    
    def get_first_result_employee_name(self) -> str:
        """Get the employee name from first search result"""
        try:
            wait_for_element_visible(self.page, self.search_results_table, timeout=5000)
            first_cell = self.page.locator(self.employee_name_cell).first
            return first_cell.inner_text().strip()
        except:
            return ""
    
    def reset_search(self):
        """Reset search filters"""
        try:
            self.page.click(self.reset_button)
            self.page.wait_for_load_state("networkidle")
        except:
            pass


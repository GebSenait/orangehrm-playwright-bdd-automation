"""
Search Page Object Model for OrangeHRM Employee Search
"""
from playwright.sync_api import Page  # type: ignore
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
        # Wait for page to be ready after login
        self.page.wait_for_load_state("networkidle", timeout=60000)
        self.page.wait_for_timeout(2000)
        
        # Click PIM menu - try multiple selectors
        try:
            pim_menu = self.page.locator('a[href*="pim"], span:has-text("PIM")').first
            pim_menu.wait_for(state="visible", timeout=10000)
            pim_menu.click()
            self.page.wait_for_timeout(1000)
        except Exception as e:
            # Try alternative navigation
            self.page.locator('span:has-text("PIM")').first.click()
            self.page.wait_for_timeout(1000)
        
        # Click Employee List
        try:
            employee_list = self.page.locator('a[href*="viewEmployeeList"], a:has-text("Employee List")').first
            employee_list.wait_for(state="visible", timeout=10000)
            employee_list.click()
        except Exception as e:
            self.page.locator('a:has-text("Employee List")').first.click()
        
        self.page.wait_for_load_state("networkidle", timeout=60000)
        self.page.wait_for_timeout(2000)
        
        # Wait for search input
        try:
            self.page.locator('input[placeholder*="Employee Name"]').first.wait_for(state="visible", timeout=10000)
        except:
            pass  # Continue even if not found immediately
    
    def search_by_employee_name(self, employee_name: str):
        """
        Search for employee by name
        
        Args:
            employee_name: Name of the employee to search
        """
        # Wait for search input with multiple strategies
        try:
            # Try multiple selectors for employee name input
            employee_input = None
            selectors = [
                'input[placeholder*="Employee Name"]',
                'input[placeholder*="employee name"]',
                'input.oxd-input[placeholder*="Name"]',
                'input[class*="oxd-input"]'
            ]
            
            for selector in selectors:
                try:
                    locator = self.page.locator(selector).first
                    if locator.is_visible(timeout=3000):
                        employee_input = locator
                        break
                except:
                    continue
            
            if not employee_input:
                # Fallback: wait a bit and try again
                self.page.wait_for_timeout(2000)
                employee_input = self.page.locator('input[placeholder*="Employee Name"]').first
                employee_input.wait_for(state="visible", timeout=10000)
            
            employee_input.fill(employee_name)
            
            # Wait for autocomplete suggestions
            self.page.wait_for_timeout(1500)
            
            # Select first suggestion if available
            try:
                suggestion = self.page.locator('div.oxd-autocomplete-option, div[role="option"]').first
                if suggestion.is_visible(timeout=2000):
                    suggestion.click()
            except:
                pass
            
            # Click search button
            try:
                search_btn = self.page.locator('button[type="submit"]:has-text("Search"), button:has-text("Search")').first
                if not search_btn.is_visible(timeout=2000):
                    search_btn = self.page.locator('button[type="submit"]').first
                search_btn.click()
            except:
                self.page.locator('button[type="submit"]').first.click()
            
            self.page.wait_for_load_state("networkidle", timeout=60000)
        except Exception as e:
            # Last resort: try basic fill and submit
            self.page.fill('input[placeholder*="Employee Name"]', employee_name)
            self.page.wait_for_timeout(1000)
            self.page.click('button[type="submit"]')
            self.page.wait_for_load_state("networkidle", timeout=60000)
    
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
            # Wait for results table
            self.page.wait_for_timeout(2000)
            
            # Wait for table to be visible
            try:
                self.page.locator('div.oxd-table-body, div[class*="oxd-table-body"]').first.wait_for(state="visible", timeout=5000)
            except:
                return ""
            
            # Get first row
            try:
                first_row = self.page.locator('div.oxd-table-row').first
                if not first_row.is_visible(timeout=3000):
                    return ""
                
                # Get all cells in the first row
                cells = first_row.locator('div.oxd-table-cell')
                cell_count = cells.count()
                
                # Employee name is typically in the second or third cell (after ID)
                # Look for a cell that contains letters (not just numbers)
                for i in range(min(cell_count, 5)):  # Check first 5 cells
                    try:
                        cell = cells.nth(i)
                        if cell.is_visible(timeout=1000):
                            cell_text = cell.inner_text().strip()
                            # Check if it looks like a name (contains letters, not just numbers)
                            if cell_text and any(c.isalpha() for c in cell_text):
                                # Return the first cell that has letters (likely the name)
                                return cell_text
                    except:
                        continue
                
                # Fallback: return text from second cell
                if cell_count > 1:
                    try:
                        second_cell = cells.nth(1)
                        if second_cell.is_visible(timeout=1000):
                            return second_cell.inner_text().strip()
                    except:
                        pass
                
                # Last resort: get all text from row and extract name
                row_text = first_row.inner_text()
                # Split and find text that looks like a name
                parts = row_text.split()
                for part in parts:
                    if any(c.isalpha() for c in part) and len(part) > 2:
                        return part
                
            except Exception as e:
                return ""
            
            return ""
        except Exception as e:
            return ""
    
    def reset_search(self):
        """Reset search filters"""
        try:
            self.page.click(self.reset_button)
            self.page.wait_for_load_state("networkidle")
        except:
            pass


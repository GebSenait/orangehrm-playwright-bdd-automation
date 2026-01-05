# Step Definitions Navigation Map

This document maps all feature file steps to their corresponding step definitions and page object methods.

## Search Feature Steps (`features/search.feature`)

| Feature Step | Step Definition File | Function Name | Page Object Method |
|--------------|---------------------|---------------|-------------------|
| `Given I am logged into OrangeHRM` | `steps/common_steps.py` | `step_login_common()` | `pages/login_page.py` → `LoginPage.login()` |
| `Given I navigate to the Employee List page` | `steps/search_steps.py` | `step_navigate_to_employee_list()` | `pages/search_page.py` → `SearchPage.navigate_to_employee_list()` |
| `When I search for an employee with name "<name>"` | `steps/search_steps.py` | `step_search_employee()` | `pages/search_page.py` → `SearchPage.search_by_employee_name()` |
| `When I search for an employee with invalid name "<name>"` | `steps/search_steps.py` | `step_search_invalid_employee()` | `pages/search_page.py` → `SearchPage.search_with_invalid_name()` |
| `When I apply employment status filter "<status>"` | `steps/search_steps.py` | `step_apply_employment_status_filter()` | `pages/search_page.py` → `SearchPage.apply_employment_status_filter()` |
| `When I click the search button` | `steps/search_steps.py` | `step_click_search()` | `pages/search_page.py` → Uses `search_button` selector |
| `Then I should see search results displayed` | `steps/search_steps.py` | `step_verify_search_results()` | `pages/search_page.py` → `SearchPage.get_search_results_count()` |
| `Then the search results should contain the employee name "<name>"` | `steps/search_steps.py` | `step_verify_employee_in_results()` | `pages/search_page.py` → `SearchPage.get_first_result_employee_name()` |
| `Then I should see "No Records Found" message` | `steps/search_steps.py` | `step_verify_no_records()` | `pages/search_page.py` → `SearchPage.is_no_records_found()` |
| `Then no search results should be displayed` | `steps/search_steps.py` | `step_verify_no_results()` | `pages/search_page.py` → `SearchPage.get_search_results_count()` |
| `Then I should see filtered search results` | `steps/search_steps.py` | `step_verify_filtered_results()` | `pages/search_page.py` → `SearchPage.get_search_results_count()` |
| `Then all results should match the applied filter` | `steps/search_steps.py` | `step_verify_filter_accuracy()` | `pages/search_page.py` → `SearchPage.get_search_results_count()` |

## Reports Feature Steps (`features/reports.feature`)

| Feature Step | Step Definition File | Function Name | Page Object Method |
|--------------|---------------------|---------------|-------------------|
| `Given I am logged into OrangeHRM` | `steps/common_steps.py` | `step_login_common()` | `pages/login_page.py` → `LoginPage.login()` |
| `Given I navigate to the Reports page` | `steps/report_steps.py` | `step_navigate_to_reports()` | `pages/reports_page.py` → `ReportsPage.navigate_to_reports()` |
| `When I generate an employee report` | `steps/report_steps.py` | `step_generate_report()` | `pages/reports_page.py` → `ReportsPage.generate_employee_report()` |
| `When I generate a report with employee name filter "<name>"` | `steps/report_steps.py` | `step_generate_filtered_report()` | `pages/reports_page.py` → `ReportsPage.generate_employee_report(employee_name=...)` |
| `When I attempt to generate a report with invalid or empty input` | `steps/report_steps.py` | `step_generate_invalid_report()` | `pages/reports_page.py` → `ReportsPage.generate_report_with_invalid_input()` |
| `Then the report should be generated successfully` | `steps/report_steps.py` | `step_verify_report_generated()` | `pages/reports_page.py` → `ReportsPage.is_report_generated()` |
| `Then the report should display employee data in a table format` | `steps/report_steps.py` | `step_verify_report_table()` | `pages/reports_page.py` → `ReportsPage.get_report_results_count()` |
| `Then the report results should match the applied filter` | `steps/report_steps.py` | `step_verify_filtered_report_accuracy()` | `pages/reports_page.py` → `ReportsPage.get_report_results_count()` |
| `Then an appropriate error message should be displayed` | `steps/report_steps.py` | `step_verify_error_message()` | `pages/reports_page.py` → `ReportsPage.is_error_message_displayed()` |
| `Then the system should handle the error gracefully` | `steps/report_steps.py` | `step_verify_error_handling()` | `pages/reports_page.py` → `ReportsPage.is_error_message_displayed()`, `is_no_records_found()` |

## How to Navigate

### In VS Code:

1. **Hover Navigation:**
   - Hover over any step in a `.feature` file
   - See tooltip with step definition location

2. **Click Navigation:**
   - **Ctrl+Click** (Windows/Linux) or **Cmd+Click** (Mac) on any step
   - Navigate directly to the step definition function

3. **Go to Definition:**
   - Place cursor on a step
   - Press **F12** or right-click → "Go to Definition"
   - Navigate to step definition

4. **Find All References:**
   - Right-click on a step definition function
   - Select "Find All References" (Shift+F12)
   - See all places where the step is used

### Step Definition Structure:

```
Feature File (features/*.feature)
    ↓ (Ctrl+Click)
Step Definition (steps/*_steps.py)
    ↓ (calls)
Page Object Method (pages/*_page.py)
```

## Troubleshooting Navigation

If navigation doesn't work:

1. **Reload VS Code Window:**
   - `Ctrl+Shift+P` → "Developer: Reload Window"

2. **Check Python Interpreter:**
   - `Ctrl+Shift+P` → "Python: Select Interpreter"
   - Choose: `.\venv\Scripts\python.exe`

3. **Verify Step Text Matches:**
   - Step text in feature file must match decorator text exactly
   - Case-sensitive matching
   - Parameter placeholders must match: `"{name}"` in both places

4. **Install Cucumber Extension:**
   - Install "Cucumber (Gherkin) Full Support" extension
   - Or "Gherkin" extension by alexkrechik


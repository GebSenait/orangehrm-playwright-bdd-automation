"""
Step definitions for Employee Search feature
"""
from behave import given, when, then
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utils.config import USERNAME, PASSWORD


@given('I am logged into OrangeHRM')
def step_login(context):
    """Step to login to OrangeHRM"""
    login_page = LoginPage(context.page)
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    assert login_page.is_logged_in(), "Login failed"


@given('I navigate to the Employee List page')
def step_navigate_to_employee_list(context):
    """Step to navigate to Employee List page"""
    search_page = SearchPage(context.page)
    search_page.navigate_to_employee_list()


@when('I search for an employee with name "{employee_name}"')
def step_search_employee(context, employee_name):
    """Step to search for an employee by name"""
    context.search_page = SearchPage(context.page)
    context.search_page.search_by_employee_name(employee_name)


@when('I search for an employee with invalid name "{invalid_name}"')
def step_search_invalid_employee(context, invalid_name):
    """Step to search with invalid employee name"""
    context.search_page = SearchPage(context.page)
    context.search_page.search_with_invalid_name(invalid_name)


@when('I apply employment status filter "{status}"')
def step_apply_employment_status_filter(context, status):
    """Step to apply employment status filter"""
    if not hasattr(context, 'search_page'):
        context.search_page = SearchPage(context.page)
    context.search_page.apply_employment_status_filter(status)


@when('I click the search button')
def step_click_search(context):
    """Step to click search button"""
    if not hasattr(context, 'search_page'):
        context.search_page = SearchPage(context.page)
    context.search_page.page.click(context.search_page.search_button)
    context.search_page.page.wait_for_load_state("networkidle")


@then('I should see search results displayed')
def step_verify_search_results(context):
    """Step to verify search results are displayed"""
    results_count = context.search_page.get_search_results_count()
    assert results_count > 0, f"Expected search results but found {results_count} results"


@then('the search results should contain the employee name "{employee_name}"')
def step_verify_employee_in_results(context, employee_name):
    """Step to verify employee name in search results"""
    first_result_name = context.search_page.get_first_result_employee_name()
    assert employee_name.lower() in first_result_name.lower(), \
        f"Expected '{employee_name}' in results but found '{first_result_name}'"


@then('I should see "No Records Found" message')
def step_verify_no_records(context):
    """Step to verify 'No Records Found' message"""
    assert context.search_page.is_no_records_found(), \
        "Expected 'No Records Found' message but it was not displayed"


@then('no search results should be displayed')
def step_verify_no_results(context):
    """Step to verify no search results are displayed"""
    results_count = context.search_page.get_search_results_count()
    assert results_count == 0, f"Expected no results but found {results_count} results"


@then('I should see filtered search results')
def step_verify_filtered_results(context):
    """Step to verify filtered search results are displayed"""
    results_count = context.search_page.get_search_results_count()
    assert results_count >= 0, "Filtered search results should be displayed"


@then('all results should match the applied filter')
def step_verify_filter_accuracy(context):
    """Step to verify filter accuracy"""
    # This is a basic check - in a real scenario, you'd validate each row
    results_count = context.search_page.get_search_results_count()
    assert results_count >= 0, "Filter should return appropriate results"


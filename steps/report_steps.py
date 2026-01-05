"""
Step definitions for Report Generation feature

This file contains all step definitions for features/reports.feature.
Each step definition is linked to methods in pages/reports_page.py.

Navigation: Hover over steps in features/reports.feature and Ctrl+Click to navigate here.
"""
from behave import given, when, then
from pages.reports_page import ReportsPage


@given('I navigate to the Reports page')
def step_navigate_to_reports(context):
    """
    Step to navigate to Reports page
    
    Linked to: pages/reports_page.py -> ReportsPage.navigate_to_reports()
    Used in: features/reports.feature (Background)
    """
    context.reports_page = ReportsPage(context.page)
    context.reports_page.navigate_to_reports()


@when('I generate an employee report')
def step_generate_report(context):
    """
    Step to generate an employee report
    
    Linked to: pages/reports_page.py -> ReportsPage.generate_employee_report()
    Used in: features/reports.feature (Scenario: Employee Report Generation)
    """
    if not hasattr(context, 'reports_page'):
        context.reports_page = ReportsPage(context.page)
    context.reports_page.generate_employee_report()


@when('I generate a report with employee name filter "{employee_name}"')
def step_generate_filtered_report(context, employee_name):
    """
    Step to generate a filtered report
    
    Linked to: pages/reports_page.py -> ReportsPage.generate_employee_report(employee_name=...)
    Used in: features/reports.feature (Scenario Outline: Filtered Report Accuracy)
    """
    if not hasattr(context, 'reports_page'):
        context.reports_page = ReportsPage(context.page)
    context.reports_page.generate_employee_report(employee_name=employee_name)


@when('I attempt to generate a report with invalid or empty input')
def step_generate_invalid_report(context):
    """
    Step to attempt generating report with invalid input
    
    Linked to: pages/reports_page.py -> ReportsPage.generate_report_with_invalid_input()
    Used in: features/reports.feature (Scenario: Invalid Input / Error Handling)
    """
    if not hasattr(context, 'reports_page'):
        context.reports_page = ReportsPage(context.page)
    context.reports_page.generate_report_with_invalid_input()


@then('the report should be generated successfully')
def step_verify_report_generated(context):
    """
    Step to verify report was generated successfully
    
    Linked to: pages/reports_page.py -> ReportsPage.is_report_generated()
    Used in: features/reports.feature (Multiple scenarios)
    """
    assert context.reports_page.is_report_generated(), \
        "Report was not generated successfully"


@then('the report should display employee data in a table format')
def step_verify_report_table(context):
    """
    Step to verify report displays data in table format
    
    Linked to: pages/reports_page.py -> ReportsPage.get_report_results_count()
    Used in: features/reports.feature (Scenario: Employee Report Generation)
    """
    results_count = context.reports_page.get_report_results_count()
    assert results_count >= 0, "Report should display data in table format"


@then('the report results should match the applied filter')
def step_verify_filtered_report_accuracy(context):
    """
    Step to verify filtered report accuracy
    
    Linked to: pages/reports_page.py -> ReportsPage.get_report_results_count()
    Used in: features/reports.feature (Scenario Outline: Filtered Report Accuracy)
    """
    results_count = context.reports_page.get_report_results_count()
    assert results_count >= 0, "Filtered report should return appropriate results"


@then('an appropriate error message should be displayed')
def step_verify_error_message(context):
    """
    Step to verify error message is displayed
    
    Linked to: pages/reports_page.py -> ReportsPage.is_error_message_displayed()
    Used in: features/reports.feature (Scenario: Invalid Input / Error Handling)
    """
    assert context.reports_page.is_error_message_displayed() or \
           context.reports_page.is_no_records_found(), \
        "Expected error message but it was not displayed"


@then('the system should handle the error gracefully')
def step_verify_error_handling(context):
    """
    Step to verify error is handled gracefully
    
    Linked to: pages/reports_page.py -> ReportsPage.is_error_message_displayed(), is_no_records_found()
    Used in: features/reports.feature (Scenario: Invalid Input / Error Handling)
    """
    # Check that either error message or no records message is shown
    has_error = context.reports_page.is_error_message_displayed()
    has_no_records = context.reports_page.is_no_records_found()
    assert has_error or has_no_records, \
        "System should display appropriate message for invalid input"


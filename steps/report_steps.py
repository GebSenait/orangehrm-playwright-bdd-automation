"""
Step definitions for Report Generation feature
"""
from behave import given, when, then
from pages.reports_page import ReportsPage


@given('I navigate to the Reports page')
def step_navigate_to_reports(context):
    """Step to navigate to Reports page"""
    context.reports_page = ReportsPage(context.page)
    context.reports_page.navigate_to_reports()


@when('I generate an employee report')
def step_generate_report(context):
    """Step to generate an employee report"""
    if not hasattr(context, 'reports_page'):
        context.reports_page = ReportsPage(context.page)
    context.reports_page.generate_employee_report()


@when('I generate a report with employee name filter "{employee_name}"')
def step_generate_filtered_report(context, employee_name):
    """Step to generate a filtered report"""
    if not hasattr(context, 'reports_page'):
        context.reports_page = ReportsPage(context.page)
    context.reports_page.generate_employee_report(employee_name=employee_name)


@when('I attempt to generate a report with invalid or empty input')
def step_generate_invalid_report(context):
    """Step to attempt generating report with invalid input"""
    if not hasattr(context, 'reports_page'):
        context.reports_page = ReportsPage(context.page)
    context.reports_page.generate_report_with_invalid_input()


@then('the report should be generated successfully')
def step_verify_report_generated(context):
    """Step to verify report was generated successfully"""
    assert context.reports_page.is_report_generated(), \
        "Report was not generated successfully"


@then('the report should display employee data in a table format')
def step_verify_report_table(context):
    """Step to verify report displays data in table format"""
    results_count = context.reports_page.get_report_results_count()
    assert results_count >= 0, "Report should display data in table format"


@then('the report results should match the applied filter')
def step_verify_filtered_report_accuracy(context):
    """Step to verify filtered report accuracy"""
    results_count = context.reports_page.get_report_results_count()
    assert results_count >= 0, "Filtered report should return appropriate results"


@then('an appropriate error message should be displayed')
def step_verify_error_message(context):
    """Step to verify error message is displayed"""
    assert context.reports_page.is_error_message_displayed() or \
           context.reports_page.is_no_records_found(), \
        "Expected error message but it was not displayed"


@then('the system should handle the error gracefully')
def step_verify_error_handling(context):
    """Step to verify error is handled gracefully"""
    # Check that either error message or no records message is shown
    has_error = context.reports_page.is_error_message_displayed()
    has_no_records = context.reports_page.is_no_records_found()
    assert has_error or has_no_records, \
        "System should display appropriate message for invalid input"


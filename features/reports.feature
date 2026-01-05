Feature: Report Generation Validation
  As a HR administrator
  I want to generate employee reports in OrangeHRM
  So that I can analyze and track employee data

  Background:
    Given I am logged into OrangeHRM
    And I navigate to the Reports page

  @reports @generation
  Scenario: Employee Report Generation
    When I generate an employee report
    Then the report should be generated successfully
    And the report should display employee data in a table format

  @reports @filtered
  Scenario: Filtered Report Accuracy
    When I generate a report with employee name filter "John"
    Then the report should be generated successfully
    And the report results should match the applied filter

  @reports @error
  Scenario: Invalid Input / Error Handling
    When I attempt to generate a report with invalid or empty input
    Then an appropriate error message should be displayed
    And the system should handle the error gracefully


Feature: Employee Search Validation
  As a HR administrator
  I want to search for employees in OrangeHRM
  So that I can find and manage employee records efficiently

  Background:
    Given I am logged into OrangeHRM
    And I navigate to the Employee List page

  @search @valid
  Scenario: Valid Employee Search
    When I search for an employee with name "John"
    Then I should see search results displayed
    And the search results should contain the employee name "John"

  @search @invalid
  Scenario: Invalid / No-Result Search
    When I search for an employee with invalid name "NonExistentEmployee123"
    Then I should see "No Records Found" message
    And no search results should be displayed

  @search @filter
  Scenario: Filter-Based Search Validation
    When I apply employment status filter "Full-Time Permanent"
    And I click the search button
    Then I should see filtered search results
    And all results should match the applied filter


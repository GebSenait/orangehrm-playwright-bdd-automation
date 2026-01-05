Feature: Employee Search Validation
  As a HR administrator
  I want to search for employees in OrangeHRM
  So that I can find and manage employee records efficiently

  Background:
    Given I am logged into OrangeHRM
    And I navigate to the Employee List page

  @search @valid
  Scenario Outline: Valid Employee Search
    When I search for an employee with name "<employee_name>"
    Then I should see search results displayed
    And the search results should contain the employee name "<employee_name>"

    Examples:
      | employee_name |
      | John          |
      | Peter         |
      | Linda         |

  @search @invalid
  Scenario Outline: Invalid / No-Result Search
    When I search for an employee with invalid name "<invalid_name>"
    Then I should see "No Records Found" message
    And no search results should be displayed

    Examples:
      | invalid_name            |
      | NonExistentEmployee123  |
      | InvalidUser999          |
      | TestUserXYZ             |

  @search @filter
  Scenario Outline: Filter-Based Search Validation
    When I apply employment status filter "<employment_status>"
    And I click the search button
    Then I should see filtered search results
    And all results should match the applied filter

    Examples:
      | employment_status      |
      | Full-Time Permanent    |
      | Part-Time Permanent    |
      | Contract               |


Feature: Login and Inventory Validation

  Scenario: Successful Login
    Given I am on the Demo Login Page
    When I fill the account information for account standard_user into the Username field and secret_sauce into the Password field
    And I click the Login Button
    Then I am redirected to the Demo Main Page
    And I verify the App Logo exists

  Scenario: Failed Login
    Given I am on the Demo Login Page
    When I fill the account information for account locked_out_user into the Username field and secret_sauce into the Password field
    And I click the Login Button
    Then I verify the error message "Epic sadface: Sorry, this user has been locked out."

  Scenario: Extract Data
    Given I am logged in
    When I am on the inventory page
    Then I extract content from the web page And save it to a text file
    Then I log out
    And I verify I am on the Login page again
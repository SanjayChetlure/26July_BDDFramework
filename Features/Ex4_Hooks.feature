
Feature: Login to application


  Scenario: S1-login to app with valid credentials
    Given user open browser
    When user enter url
    And user enter username
    And user enter password
    And user click on login btn
    Then user should be at home page


  Scenario: S2-login to app with invalid credentials
    Given user open browser
    When user enter url
    And user enter invalid username
    And user enter invalid password
    And user click on login btn
    Then user can see error msg
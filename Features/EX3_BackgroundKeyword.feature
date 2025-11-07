Feature: Login to application

  Background:
    Given user open browser
    When user enter url


  Scenario: S1-login to app with valid credentials
    And user enter username
    And user enter password
    And user click on login btn
    Then user should be at home page


  Scenario: S2-login to app with invalid credentials
    And user enter invalid username
    And user enter invalid password
    And user click on login btn
    Then user can see error msg
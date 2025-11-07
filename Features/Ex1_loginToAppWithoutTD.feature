Feature: Login to application
  Scenario: login to app without Test Data
    Given user open browser
    When user enter url
    And user enter username
    And user enter password
    And user click on login btn
    Then user should be at home page
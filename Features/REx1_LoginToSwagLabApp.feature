@regression
Feature: login to swag lab application
Background:
  Given user is on swagLab login page

  @smoke
  Scenario: S1-Login to SwagLab app using valid credentials
    When user enter username "UN" on swagLab login page
    And user enter password "PWD" on swagLab login page
    And user clicks login btn on swagLab login page
    Then user should be on swagLab home page with logoText "Swag Labs1s"

  @sanity
  Scenario: s2- login to swaglab app using invalid credentials
    When user enter username "UN" on swagLab login page
    And user enter password "WrongPWD" on swagLab login page
    And user clicks login btn on swagLab login page
    Then error message is visible


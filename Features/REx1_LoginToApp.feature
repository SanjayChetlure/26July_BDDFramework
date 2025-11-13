Feature: login to swag lab application

  Scenario: S1-Login to SwagLab app using valid credentials
    Given user is on swagLab login page
    When user enter username "standard_user" on swagLab login page
    And user enter password "secret_sauce" on swagLab login page
    And user clicks login btn on swagLab login page
    Then user should be on swagLab home page with logoText "Swag Labs"


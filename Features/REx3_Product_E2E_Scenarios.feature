Feature: E2E-Product features

  Background:
    Given user is on swagLab login page
    When user enter username "UN" on swagLab login page
    And user wait for "1" sec
    And user enter password "PWD" on swagLab login page
    And user wait for "1" sec
    And user clicks login btn on swagLab login page
    And user wait for "1" sec
    When user is on SwagLab home page

  Scenario: S6-Place order - E2E
    When user click on addToCart btn
    And user wait for "1" sec
    And user click on cart link
    And user wait for "1" sec

    And user is on SwagLab yourCart page
    And user click on checkout button

    And user is on SwagLab checkout yourInfo page
    And user enter FN as "abc"
    And user wait for "1" sec
    And user enter LN as "xyz"
    And user wait for "1" sec
    And user enter ZipCode "12345"
    And user wait for "1" sec
    And user click on continue button

    And user is on SwagLab checkout Overview page
    And user click on finish button
    And user wait for "1" sec

    And user is on SwagLab checkout complete page
    Then order placed message visible
#    And user wait for "5" sec







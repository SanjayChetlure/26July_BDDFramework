Feature: E2E-Product features Scenario outline

  Background:
    Given user is on swagLab login page
    When user enter username "UN" on swagLab login page
    And user wait for "1" sec
    And user enter password "PWD" on swagLab login page
    And user wait for "1" sec
    And user clicks login btn on swagLab login page
    And user wait for "1" sec
    When user is on SwagLab home page

  Scenario Outline: S7 - E2E scenario using scenario outline
    When user click on addToCart btn
    And user wait for "1" sec
    And user click on cart link
    And user wait for "1" sec
    And user is on SwagLab yourCart page
    And user click on checkout button
    And user is on SwagLab checkout yourInfo page
    And user enter FN as "<firstname>"
    And user wait for "1" sec
    And user enter LN as "<lastname>"
    And user wait for "1" sec
    And user enter ZipCode "<postalCode>"
    And user wait for "1" sec
    And user click on continue button
    And user is on SwagLab checkout Overview page
    And user click on finish button
    And user wait for "1" sec
    And user is on SwagLab checkout complete page
    Then order placed message visible

    Examples:
      | firstname  | lastname | postalCode |
      |  abc1      |   xyz1   |   123456   |
      |  abc2      |   xyz2   |   232132   |
      |  abc3      |   xyz3   |   232147   |









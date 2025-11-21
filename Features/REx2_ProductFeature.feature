Feature: product features
  @addToCart
  Scenario: add to cart button functionality
    Given user is on swagLab login page
    When user enter username "UN" on swagLab login page
    And user wait for "2" sec
    And user enter password "PWD" on swagLab login page
    And user wait for "2" sec
    And user clicks login btn on swagLab login page
    And user wait for "2" sec
    And user click on addToCart btn
    And user wait for "2" sec
    Then remove btn is visible
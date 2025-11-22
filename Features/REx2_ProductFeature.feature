Feature: product features

  Background:
    Given user is on swagLab login page
    When user enter username "UN" on swagLab login page
    And user wait for "1" sec
    And user enter password "PWD" on swagLab login page
    And user wait for "1" sec
    And user clicks login btn on swagLab login page
    And user wait for "1" sec
    When user is on SwagLab home page


  Scenario: S3-add to cart button functionality
    And user click on addToCart btn
    And user wait for "2" sec
    Then remove btn is visible


  Scenario: S4-verify total product count on home page
    Then verify total "6" products are available on home page


  @addToCart
  Scenario: S5-verify price on specific product
    Then verify price of product Sauce Labs Backpack is "29.99"


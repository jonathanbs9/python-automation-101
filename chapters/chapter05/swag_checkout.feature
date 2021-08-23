Feature: Checkout

  Scenario: Checkout successfully with a single item
    Given I add an item to the cart
    When I checkout
    And fill the form
    Then I see "THANK YOU FOR YOUR ORDER"
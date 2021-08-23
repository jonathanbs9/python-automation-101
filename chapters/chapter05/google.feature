Feature: Google Search

    Scenario: Entering a search displays a Result Page
        Given I am on a Google search
        When I search "ovejeros alemanes"
        Then I see the "ovejeros alemanes" Result Page
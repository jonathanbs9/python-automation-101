Feature: Sort the product catalog

    As a shopper
    I want different ways to sort the products
    so it`s easier for me to find what I`m looking for

    Scenario: Sort by Name from Z to A
        Given The Product Page
        When I change the sort to "Name (Z to A)"
        Then the products should be in descending order
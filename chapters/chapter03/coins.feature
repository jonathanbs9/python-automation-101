Feature: Change for a Dollar

    Feature Description

    Scenario: Calculate the sum of pennies
        Given the input is '50'
        Then the sum should be 50
    
    Scenario: Calculate the sum of nickels
        Given the input is '5'
        Then the sum should be 25
    
    Scenario: Calculate the sum of dimmes
        Given the input is '15'
        Then the sum should be 150
    
    Scenario: Calculate the sum of quarters
        Given the input is '4'
        Then the sum should be 100
    
    Scenario: Calculate the sum of all coins
        Given the input is '1' penny
        And '1' nickel
        And '1' dime
        And '1' quarter
        Then the sum should be 41
    
    Scenario Outline: Generate Game Result message
        Given the grand total is {total}
        When the result is calculated
        Then the message should be {message}

    Examples:
        | total | message | 
        | 59    | 'You lose .. You were under 41 cents' | 
        | 150   | 'You lose .. You are over 50 cents'   | 
        | 100   | 'You win! =) You have 0 dif'           |
Feature: SwagLab Login 

    Scenario: User can login successfully
        Given I am on the login page
        When I enter a valid username and a valid password
        Then I land on the Products page

    Scenario: User can logout
        Given I am logged in on the Product Page
        When I log out
        Then I land on the Login Page

    Scenario Outline: User can not login with invalid username and password
        Given the Login Page
        When I click login with and invalid {username} or {password}
        Then I see an error {message}
    
    Examples:
        | username        | password          | message |
        | 'invalid_user'  | 'secret_sauce'    | 'Username and password do not match any user in this service'  |
        | 'standard_user' | 'invalid_password'| 'Username and password do not match any user in this service'  |
        | 'invalid_user'  | 'invalid_password'| 'Username and password do not match any user in this service'  |
        | ''              | 'secret_sauce'    | 'Username is required'                                         |
        | 'standard_user' | ''                | 'Password is required'                                         |
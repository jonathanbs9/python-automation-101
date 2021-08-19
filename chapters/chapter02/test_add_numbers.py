from add_numbers import add, is_even, convert_to_number

# Scenario
# Feature: Add two numbers to get their sum
# Scenario: Adding two even numbers returns an even number

def test_convert_string_to_number():
    number = convert_to_number("5")
    assert number == 5

def test_convert_string_to_negative_number():
    number = convert_to_number("-5")
    assert number == -5
    
def test_string_input():
    output = add("Jonathan", 9)
    assert output == "Invalid numbers entered!"
    

def test_2_is_even():
    assert is_even(4)

def test_5_is_odd():
    assert is_even(5) is False


# Given x=2 and y=2
# When I add them together
# Then the sum should be 4 and be even

def test_adding_even_numbers_returns_even_number():
    number = add(2, 2)
    assert number == 4
    assert is_even(number)

# Given x=-9 and y=-9
# When I add them together
# The the sum should be -18 and negative
def test_adding_negative_numbers_returns_negative_number():
    number = add(-9 , -9)
    assert number == -18

# Given x=8 and y=-1
# When I add them together
# The the sum should be 7 and positive
def test_adding_even_and_odd_numbers_returns_positive_if_greater():
    number = add(8, -1)
    assert number == 7
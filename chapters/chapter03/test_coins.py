from coins import sum_all_coins, sum_dimmes, sum_nickels, sum_quarters, sum_pennies
import pytest


# 1 cent
def test_sum_pennies():
    total = sum_pennies(user_input='50')
    assert total == 50

# 5 cents
def test_sum_nickels():
    total = sum_nickels(user_input='5')
    assert total == 25

# 10 cents
def test_sum_dimes():
    total = sum_dimmes(user_input='15')
    assert total == 150

# 25 cents
def test_sum_quarters():
    total = sum_quarters(user_input='4')
    assert total == 100

def test_sum_all_coins():
    total = sum_all_coins(pennies='1',nickels='1',dimes='1',quarters='1')
    assert total == 41
    

def test_win_the_exact_dollar():
    total = sum_all_coins('15','8','2','1')
    dif = 0
    message = ''
    if total == 100:
        dif = 100 - total
        message = f'You win! =) You have {dif} dif'
    assert dif == 0
    assert message == 'You win! =) You have 0 dif'

def test_lose_with_less_than_dollar():
    total = sum_all_coins('1','1','1','1')
    dif = 0
    message = ''
    if total < 100:
        dif = 100 - total
        message = f'You lose .. You were under {dif} cents'
    assert dif == 59
    assert message == 'You lose .. You were under 59 cents'


def test_lose_with_more_than_dollar():
    total = sum_all_coins('50','40','30','20')
    dif =  0
    message =  ''
    if total > 100:
        dif = total - 100
        message = f'You lose .. You are over {dif} cents'
    assert dif == 950
    assert message == 'You lose .. You are over 950 cents'




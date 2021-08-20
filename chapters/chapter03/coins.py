def sum_pennies(user_input):
    pennies = int(user_input) * 1
    return pennies

def sum_nickels(user_input):
    nickels = int(user_input) * 5
    return nickels

def sum_dimmes(user_input):
    dimmes = int(user_input) * 10
    return dimmes

def sum_quarters(user_input):
    quarters = int(user_input) * 25
    return quarters

def sum_all_coins(pennies,nickels,dimes,quarters):
    return sum([sum_pennies(pennies),sum_nickels(nickels), sum_dimmes(dimes), sum_quarters(quarters)])

def lose_with_less_than_dollar(total):
    under = 0
    message = ''
    if total < 100:
        under = 100 - total
        message = f'You lose .. You were under {under} cents'
    
    return under, message

def lose_with_more_than_dollar(total):
    over = 0
    message = ''
    if total > 100:
        over = total - 100
        message = f'You lose .. You are over {over} cents'
    
    return over, message

def generate_result(total):
    if total == 100:
        return 'You win! =) You have 0 dif'
    
    if total < 100:
        under = 100 - total
        return f'You lose .. You were under {under} cents'

    if total > 100:
        over = total - 100
        return f'You lose .. You are over {over} cents'
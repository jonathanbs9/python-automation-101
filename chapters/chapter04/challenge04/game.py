import random

def start_game() -> dict:
    return {
        'counter' : 1,
        'current_space': 0
    }

def roll_die() -> int:
    roll = random.randint(1,6)
    return roll

def advance_player(game_state: dict, roll: int)-> str:
    GOAL = 20
    landing_space = game_state['current_space'] + roll
    message = 'Roll {0}: You rolled a {1}. '.format(game_state['counter'], roll) 

    if landing_space == GOAL:
        message += f'You are on space {GOAL}. You win!'
    
    if landing_space > GOAL:
        difference = landing_space - GOAL
        message += f'You lose. You overshot the goal by {difference}.'
    
    if landing_space < GOAL:
        remaining = GOAL - landing_space
        game_state['counter'] +=1
        game_state['current_space'] = landing_space
        message += f'You are on space {landing_space} and have {remaining} more to go!'
    
    return message
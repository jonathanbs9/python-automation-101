import game

def roll_the_die_game():
    MAX_TURNS = 5 
    message= ''
    game_state = game.start_game()

    while game_state['counter'] <= MAX_TURNS:
        roll = game.roll_die()
        message = game.advance_player(game_state, roll)
        print(message)

        if 'lose' in message or 'win' in message:
            break
        
    if 'more to go' in message:
        print('You run out of rolls =( ')

if __name__ == '__main__':
    roll_the_die_game()
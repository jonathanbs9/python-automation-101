from game import roll_die, start_game, advance_player

def test_roll_die():
    roll = roll_die()
    dice_numbers = [1,2,3,4,5,6]
    assert roll in dice_numbers

def test_initiate_game_state_object():
    game_state= start_game()
    assert game_state == {'counter':1, 'current_space':0}

def test_player_under_goal():
    roll = 5
    game_state = { 'counter': 1, 'current_space': 0}
    message = advance_player(game_state, roll)
    assert message == 'Roll 1: You rolled a 5. You are on space 5 and have 15 more to go!'

# Complete more tests
from count_vowels import count_vowels
import pytest

def test_sentence():
    user_input = 'Jonathan is now testing function'
    vowels =  'aeiou'
    count = 0
    for character in user_input.lower():
        if character in vowels:
            count +=1
    assert count == 10

def test_count_vowels_with_sentence():
    user_input = 'Jonathan is now testing function'
    count = count_vowels(user_input)
    assert count == 10

def test_count_vowels_with_uppercase():
    user_input = 'JONATHAN IS NOW TESTING FUNCTION'
    count = count_vowels(user_input)
    assert count == 10

examples = [
    ('zzz', 0),
    ('abc', 1),
    ('', 0),
    ('Iphone', 3)
]

@pytest.mark.parametrize('word, count', examples)
def test_count_vowels_with_single_word(word, count):
    number_of_vowels = count_vowels(word)
    assert count == number_of_vowels
from count_vowels import count_vowels

def program():
    user_input = input('Enter a word or a sentence: ')
    count = count_vowels(user_input)
    print(f'The word or sentence has {count} vowels')

if __name__ == '__main__':
    program()
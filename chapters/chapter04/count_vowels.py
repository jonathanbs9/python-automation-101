def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for character in string.lower():
        if character in vowels:
            count +=1
    return count
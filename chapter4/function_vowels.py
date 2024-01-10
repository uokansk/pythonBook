def search_for_vowels(word):
    """Выводит гласные найденные указанном в слове"""
    vowels = set('aeiou')
    # word = input('Provide a word to search for vowels: ')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


# str 191

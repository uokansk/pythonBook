def search4vowels(phrase: str) -> set:
    """Возвращает гласные найденные в указанной фразе"""
    letters = set('aeiou')
    return letters.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    return set(letters).intersection(set(phrase))


# found = search4letters('Returns vowels found in the specified phrase')
# print(found)

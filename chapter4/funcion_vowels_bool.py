def search4vowels(word: str) -> set:
    """Возвращает булевое значение в зависимости от присутствия любых гласных"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found


if __name__ == '__main__':
    sol = search4vowels('sky')
    print(sol)

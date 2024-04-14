def search4vowels(phrase: str) -> set:
    """Возвращает гласные найденные в указанной фразе"""
    letters = set('aeiou')
    return letters.intersection(set(phrase))

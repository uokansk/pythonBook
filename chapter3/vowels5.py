vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
print(found)
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
        # if letter in found:
        #     found[letter] += 1
        # else:
        #     found[letter] = 1
print(found)

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
print(sorted(found.items()))

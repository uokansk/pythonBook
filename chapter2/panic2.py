# on tap
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

first_word = ''.join(plist[1:3])
second_word = ''.join(plist[-5:-7:-1])

new_phrase = first_word + ''.join([plist[5], plist[4]]) + second_word
print(plist)
print(new_phrase)

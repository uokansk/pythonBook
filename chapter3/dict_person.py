person3 = {'1_Name': 'Ford Prefect',
           '2_Gender': 'Male',
           '3_Occupation': 'Researcher',
           '4_Home Planet': 'Betelgeuse Seven'}
# key_person = input('Enter key person3: ')
# print(person3[key_person])
for kv in person3:
    print(kv, ':', person3[kv])
print()

# использование items

for k, v in sorted(person3.items()):
    print(k, ':', v)

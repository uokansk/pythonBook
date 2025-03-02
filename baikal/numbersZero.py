a = [-9, -6, 7, 2, 6, -4, -10, -11, 11, 14, 20, -12, -20, -2, -14, -6, -3, 14]
b = [-14, -3, -3, -6]
[i for i in a if not i in b]
set_b = set(b)
# deduped = list(dict.fromkeys(b))
c = a.copy()
d = [x for x in a if not x in set(b)]
# for i in a:
#     # print('i=',i)
#     for j in set_b:
#         # print('j=', j)
#         if i == j:
#             c.remove(i)

# x for x in a if x not in b
print(c)
print(a)
print(set_b)
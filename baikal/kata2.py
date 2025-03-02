# In this kata you will create a function that takes a list of non-negative integers and strings and
# returns a new list with the strings filtered out.
a = [1, 2, 'aasf', '1', '123', 123]
c=[]

for i in a:
    if type(i) == int:
        c.append(i)
print(i for i in a if type(i) == int)
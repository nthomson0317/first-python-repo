

l = [1,2,2,3,3,3,4,3,3,3,2,2,1]

d = {}

for index, value in enumerate(l):
    d[index] = value

print('dict: ')
print(d)

rev_multidict = {}
for key, value in d.items():
    rev_multidict.setdefault(value, set()).add(key)

print('rev multidict: ')
print(rev_multidict)
x = {'key':1234}
print(x['key'])

x['key2'] = 4
print(x)

x[2] = 8
print(x)

print('key' in x)
print(list(x.values()))

del x['key']

for key,value in x.items():
    print(key,value)

for key in x:
    print(key)

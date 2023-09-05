string = input("Enter String: ")
dict = { }

for word in string.split(' '):
    if word in dict.keys():
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1
    
for key, value in dict.items():
    print(key, value)
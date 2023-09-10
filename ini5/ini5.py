data = open("dataset.txt", "r")
output = open("output.txt", "w")
string = data.read()
list = string.split("\n")
i = 1
for word in range(len(list)):
    if i < len(list):
        output.write(list[i] + '\n')
        i += 2
    else:
        print("Done")
        quit()
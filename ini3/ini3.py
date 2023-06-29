string = input("Enter string: ")
# 22 27 97 102
point_a = int(input("a: "))
point_b = int(input("b: "))
point_c = int(input("c: "))
point_d = int(input("d: "))

word_1 = string[point_a: point_b + 1]
word_2 = string[point_c: point_d + 1]
print(word_1, word_2)
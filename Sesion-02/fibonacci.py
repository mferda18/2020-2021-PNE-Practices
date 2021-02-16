my_list = [0, 1]
a = 0
b = 1
for i in range(1, 10):
    c = a + b
    my_list.append(c)
    a = b
    b = c
print(my_list)
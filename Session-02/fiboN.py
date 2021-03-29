def fibon(n):
    my_list = [0, 1]
    a = 0
    b = 1
    for i in range(1, n):
        c = a + b
        my_list.append(c)
        a = b
        b = c
    return my_list[-1]


# -- The main program starts here
print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))
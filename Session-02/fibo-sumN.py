def fibosum(n):
    my_list = [0, 1]
    a = 0
    b = 1
    sum = 0
    for i in range(1, n):
        c = a + b
        my_list.append(c)
        a = b
        b = c
    for n in my_list:
        sum += n
    return sum


# -- The main program starts here
print("Sum of the first 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series: ", fibosum(10))
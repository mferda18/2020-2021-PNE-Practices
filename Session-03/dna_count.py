def count_dna(sequence):
    a, c, g, t = 0, 0, 0, 0
    for e in sequence:
        if e == "A":
            a += 1
        if e == "C":
            c += 1
        if e == "G":
            g += 1
        if e == "T":
            t += 1
    return a, c, g, t


# -- The main program starts here
my_dna = input("Introduce the sequence: ")
a, c, g, t = count_dna(my_dna)
print("Total length:", a + c + g + t)
print("A:", a)
print("C:", c)
print("T:", t)
print("G:", g)
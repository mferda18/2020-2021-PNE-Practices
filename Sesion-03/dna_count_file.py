def correct_sequence(dna):
    for i in dna:
        if i != "A" and i != "C" and i != "G" and i != "T":
            return False
        return True

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

def read_from_file(filename):
    with open(filename, "r") as f:
        dna = f.read()
        dna = dna.replace("\n", "")
        return dna

our_dna = read_from_file("dna.txt")
if correct_sequence(our_dna):
    print("Total sequence", len(our_dna))
    c, t, g, a = count_dna(our_dna)
    print("A:", a)
    print("G:", g)
    print("C:", c)
    print("T:", t)
else:
    print("Incorrect program")

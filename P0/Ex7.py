import Seq0

FOLDER = "./sequences/"
ID = "U5.txt"

frag, comp = Seq0.seq_complement(FOLDER + ID)

print("------| Exercise 7 |------\nGene U5:")
print("Frag:", frag, "\nComp:", comp)

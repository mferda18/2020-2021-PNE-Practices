from Seq1 import Seq

PROJECT_PATH = "./PROJECTS/"

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Exercise 10 |------")
for gene in gene_list:
    sequence = Seq()
    sequence.read_fasta(PROJECT_PATH + gene + ".txt")
    print("Gene", gene, ": Most frequent Base:", sequence.frequent_base())
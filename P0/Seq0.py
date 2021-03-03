from pathlib import Path

def seq_ping():
    print("OK")

def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")

def seq_read_fasta(filename):
    return take_out_first_line(Path(filename).read_text())

def seq_len(seq):
    return(len(seq))

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    gene_dict = {"A": 0, "T": 0, "C": 0, "G": 0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict

def seq_reverse(seq):
    fragment = seq_read_fasta(seq)[0:20]
    reverse = fragment[::-1]
    return fragment, reverse

def seq_complement(seq):
    fragment = seq_read_fasta(seq)[0:20]
    comp = ""
    for b in fragment:
        if b == "A":
            comp += "T"
        if b == "C":
            comp += "G"
        if b == "T":
            comp += "A"
        if b == "G":
            comp += "C"
    return fragment, comp

def frequent_base(seq):
    gene_dict = {"A": 0, "T": 0, "C": 0, "G": 0}
    for d in seq:
        gene_dict[d] += 1
    key_list = list(gene_dict.keys())
    count = list(gene_dict.values())
    most_frequent = max(count)
    position = count.index(most_frequent)
    return key_list[position]


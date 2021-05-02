import termcolor
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    #Inside of a class the order of the sequences does not matter
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, strbases = NULL_SEQUENCE):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL Seq created")
            self.strbases = strbases
        else:
            if Seq.is_valid_sequence_2(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT Sequence detected")

    @staticmethod
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence" + str(i) + ": (Length: " + str(list_sequences[i].len()) + ") " + str(list_sequences[i])
            termcolor.cprint(text, "yellow")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not (self.strbases == Seq.NULL_SEQUENCE) and not (self.strbases == Seq.INVALID_SEQUENCE):
            for e in self.strbases:
                if e == "A":
                    a += 1
                if e == "C":
                    c += 1
                if e == "G":
                    g += 1
                if e == "T":
                    t += 1
        return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A": a, "C": c, "T": t, "G": g}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            complement = ""
            for e in self.strbases:
                if e == "A":
                    complement += "T"
                if e == "C":
                    complement += "G"
                if e == "G":
                    complement += "C"
                if e == "T":
                    complement += "A"
            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())
        return self.strbases

    def frequent_base(self):
        gene_dict = {"A": 0, "T": 0, "C": 0, "G": 0}
        for d in self.strbases:
            gene_dict[d] += 1
        key_list = list(gene_dict.keys())
        count = list(gene_dict.values())
        most_frequent = max(count)
        position = count.index(most_frequent)
        return key_list[position]

    def percentage(self):
        total = len(self.strbases)
        a, c, g, t = self.count_bases()
        p_a = (a / total) * 100
        p_c = (c / total) * 100
        p_g = (g / total) * 100
        p_t = (t / total) * 100
        return p_a, p_c, p_g, p_t




def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid Sequence")
    return s1, s2, s3







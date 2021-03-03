import termcolor

class Seq:
    """A class for representing sequences"""
    #Inside of a class the order of the sequences does not matter

    def __init__(self, strbases="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == "NULL":
            print("NULL Seq created")
            self.strbases = strbases
        else:
            if Seq.is_valid_sequence_2(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = "Error"
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
        if self.strbases == "NULL" or self.strbases == "Error":
            return 0
        else:
            return len(self.strbases)


def generate_seqs(pattern, number):
    #A, 3
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq

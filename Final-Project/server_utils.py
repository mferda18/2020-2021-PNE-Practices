from Seq1 import Seq
from jinja2 import Template
import pathlib


def print_colored(message, color):
    import termcolor
    import colorama

    colorama.init(strip="False")
    print("To server: ", end="")
    print(termcolor.colored(message, color))


def format_command(command):
    return command.replace("\n", "").replace("\r", "")


def ping(cs):
    print_colored("PING command", "green")
    response = "OK!"
    cs.send(str(response).encode())
    print(response)


def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content


def get(list_sequences, seq_number):
    context = {
        "number": seq_number,
        "sequence": list_sequences[int(seq_number)]
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents


def info(sequence):
    #sequence = Seq(sequence)
    response = "Total length: " + str(sequence.len())
    response += "<br><br> A: " + str(sequence.count_bases()[0]) + " (" + str(sequence.percentage()[0]) + "%) <br><br>"
    response += "C: " + str(sequence.count_bases()[1]) + " (" + str(sequence.percentage()[1]) + "%) <br><br>"
    response += "G: " + str(sequence.count_bases()[2]) + " (" + str(sequence.percentage()[2]) + "%) <br><br>"
    response += "T: " + str(sequence.count_bases()[3]) + " (" + str(sequence.percentage()[3]) + "%) <br><br>"
    return response


def comp(sequence):
    sequence = Seq(sequence)
    response = sequence.complement()
    context = {
        "sequence": sequence,
        "operation": "comp",
        "result": response
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def rev(sequence):
    sequence = Seq(sequence)
    response = sequence.reverse()
    context = {
        "sequence": sequence,
        "operation": "rev",
        "result": response
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def gene(seq_name):
    PATH = "./sequences/" + seq_name + ".txt"
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {
        "gene_name": seq_name,
        "gene_contents": s1.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents

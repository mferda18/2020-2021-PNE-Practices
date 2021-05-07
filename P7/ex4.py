import http.client
import json
from Seq1 import Seq

DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226906",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSMUSG00000062960",
    "ANK2": "ENSG00000145362"
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMETERS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
try:
    user_gene = input("Enter the Gene that you want to analyse: ")
    my_id = DICT_GENES[user_gene]
    connection.request("GET", ENDPOINT + my_id + PARAMETERS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        #print(json.dumps(response_dict, indent=4, sort_keys=True))
        sequence = Seq(response_dict["seq"])
        s_length = sequence.len()
        percentages = sequence.percentage(sequence.count_bases(), s_length)
        most_frequent_base = sequence.frequent_base(sequence.count())
        print("Total length: ", s_length)
        for value in percentages.values():
            print(value)
        print("Most frequent base: ", most_frequent_base)
except KeyError:
    print("The gene is not inside our dictionary. Choose one of the following:", list(DICT_GENES.keys()))

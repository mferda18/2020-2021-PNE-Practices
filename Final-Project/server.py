import http.server
import http.client
import socketserver
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from jinja2 import Template
import json
from Seq1 import Seq
import server_utils as su

PORT = 8080
SERVER = "rest.ensembl.org"
params = "?content-type=application/json"

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

connection = http.client.HTTPConnection(SERVER)

socketserver.TCPServer.allow_reuse_address = True


def read_template_html_file(filename):
    content = Template(Path(filename).read_text())
    return content


def connection_ensembl(input_endpoint, input_parameters):
    connection.request("GET", input_endpoint + input_parameters)
    response = connection.getresponse().read().decode()
    dict_response = json.loads(response)
    return dict_response


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        o = urlparse(self.path)
        path_name = o.path
        parameters = parse_qs(o.query)

        print("Path:", path_name)
        print("Parameters:", parameters)

        context = {}
        species_list = []

        if path_name == "/":
            contents = read_template_html_file("html/index.html").render()
        elif path_name == "/listSpecies":
            endpoint = "/info/species"
            dict_response = connection_ensembl(endpoint, params)
            final_list = []
            try:
                values = dict_response.values()
                for d in values:
                    for i in d:
                        element = i["common_name"]
                        species_list.append(element)
                if len(parameters) == 0:
                    input_number = len(species_list)
                else:
                    input_number = parameters["limit"][0]
                input_number = int(input_number)
                if input_number < 0:
                    raise ValueError
                context["number_of_wanted_species"] = input_number
                context["total_species"] = len(species_list)
                if input_number <= len(species_list):
                    for i in range(0, input_number):
                        final_list.append(species_list[i].capitalize())
                    context["list_species"] = final_list
                else:
                    context["list_species"] = species_list
                contents = read_template_html_file("html/species_names.html").render(context=context)
            except ValueError:
                contents = read_template_html_file("html/error.html").render()
        elif path_name == "/karyotype":
            try:
                specie = parameters["specie"][0]
                if specie.find(" "):
                    specie = specie.replace(" ", "_")
                print(specie)
                endpoint = "/info/assembly/" + specie
                dict_response = connection_ensembl(endpoint, params)
                context["karyotype"] = list(dict_response["karyotype"])
                contents = read_template_html_file("html/karyotype.html").render(context=context)
            except KeyError:
                contents = read_template_html_file("html/error.html").render()
        elif path_name == "/chromosomeLength":
            try:
                specie = parameters["specie"][0]
                if specie.find(" "):
                    specie = specie.replace(" ", "_")
                endpoint = "/info/assembly/" + specie
                dict_response = connection_ensembl(endpoint, params)
                input_number = int(parameters["chromo"][0])
                context["length"] = dict_response["top_level_region"][input_number]["length"]
                contents = read_template_html_file("html/chromosomeLength.html").render(context=context)
            except (ValueError, KeyError):
                contents = read_template_html_file("html/error.html").render()
        elif path_name == "/geneSeq":
            gene = parameters["gene"][0]
            if gene in DICT_GENES.keys():
                endpoint = "/sequence/id/" + DICT_GENES[gene]
                dict_response = connection_ensembl(endpoint, params)
                print(dict_response)
                sequence = Seq(dict_response["seq"])
                context["sequence"] = sequence
                context["gene"] = gene
                contents = read_template_html_file("html/sequence.html").render(context=context)
            else:
                contents = read_template_html_file("html/error.html").render()
        elif path_name == "/geneInfo":
            gene = parameters["gene"][0]
            if gene in DICT_GENES.keys():
                endpoint = "/sequence/id/" + DICT_GENES[gene]
                dict_response = connection_ensembl(endpoint, params)
                sequence = Seq(dict_response["seq"])
                context["gene"] = gene
                context["length"] = sequence.len()
                context["id"] = dict_response["id"]
                my_list = dict_response["desc"].split(":")
                context["chromosome_name"] = my_list[2]
                start_and_end = ""
                start_and_end += my_list[3] + ", " + my_list[4]
                context["start_and_end"] = start_and_end
                contents = read_template_html_file("html/info.html").render(context=context)
            else:
                contents = read_template_html_file("html/error.html").render()
        elif path_name == "/geneCalc":
            gene = parameters["gene"][0]
            if gene in DICT_GENES.keys():
                endpoint = "/sequence/id/" + DICT_GENES[gene]
                dict_response = connection_ensembl(endpoint, params)
                sequence = Seq(dict_response["seq"])
                result = su.info(sequence)
                context["gene"] = gene
                context["result"] = result
                contents = read_template_html_file("html/calculations.html").render(context=context)
            else:
                contents = read_template_html_file("html/error.html").render()
        else:
            contents = "Error"

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()

        self.wfile.write(contents.encode())

        return


Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

import csv
import json
import re

def csv_to_json(csv_file_path):
    try:
        json_filename = re.search(r"^[^.]*", csv_file_path).group(0)
        json_filename = json_filename + ".json"
        csv = open(csv_file_path)
        json = open(json_filename, "w")
        lines = csv.readlines()
        existe_notas = False

        # se detetar que existe um campo chamado "notas"
        if re.search(r"(Notas)", lines[0]) != None:
            existe_notas = True

        numero = ""
        nome = ""
        curso = ""

        # remover a primeira linha porque não queremos que seja escrita no ficheiro json
        lines.pop(0)

        json.write("[\n")

        for line in lines:

            dict = {}

            list = line.split(",")
            dict["Número"] = list[0]
            dict["Nome"] = list[1]
            dict["Curso"] = list[2]

            if existe_notas:
                notas = []

                #criar a lista de notas
                notas = re.search(r",\b\d+(?:,\d+)*(,)?", line).group(0).split(",")

                # retirar valores nulos da lista de notas
                notas.pop(0)
                if(notas[notas.__len__() - 1] == ''):
                    notas.pop(notas.__len__() - 1)

                dict["Notas"] = notas

            json.write("\t" + dict.__str__() + "\n")
            """
            json.write("\t{\n")
            json.write("\t\tNúmero:" + dict["Número"] + "\n")
            json.write("\t\tNome:" + dict["Nome"] + "\n")
            json.write("\t\tCurso:" + dict["Curso"] + "\n")
            json.write("\t}\n")
            """
        json.write("]\n")

    finally:

        csv.close()
        json.close()

def main():

    # construção da UI
    print(" ")
    print("------------------------------ TPC 4 ------------------------------")
    print(" ")
    print("Insira qual ficheiro quer converter...")
    print(" ")
    print("-------------------------------------------------------------------")
    print(" ")

    csv_file_path = input('---> ')


    csv_to_json(csv_file_path)


if __name__ == "__main__":
    main()

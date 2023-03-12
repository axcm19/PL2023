import csv
import json
import re

#-----------------------------------------------------------------------------------------------------------------------

def maior(lista_notas):
    maior = 0

    for nota in lista_notas:
        if int(nota) > maior:
            maior = int(nota)

    return maior

#-----------------------------------------------------------------------------------------------------------------------

def menor(lista_notas):
    menor = int(lista_notas[0])

    for nota in lista_notas:
        if int(nota) < menor:
            menor = int(nota)

    return menor

#-----------------------------------------------------------------------------------------------------------------------

def media(lista_notas):
    soma = 0
    quantos = 0
    media = 0

    for nota in lista_notas:
        soma += int(nota)
        quantos += 1

    media = soma / quantos

    return media

#-----------------------------------------------------------------------------------------------------------------------

def sum(lista_notas):
    soma  =0

    for nota in lista_notas:
        soma = soma + int(nota)

    return soma

#-----------------------------------------------------------------------------------------------------------------------

def csv_to_json(csv_file_path):
    try:
        json_filename = re.search(r"^[^.]*", csv_file_path).group(0)
        json_filename = json_filename + ".json"
        csv = open(csv_file_path)
        json = open(json_filename, "w")
        lines = csv.readlines()
        existe_notas = False
        existe_func = False
        func = ""

        # se detetar que existe um campo chamado "notas"
        if re.search(r"(Notas)", lines[0]) != None:
            existe_notas = True

        # se detetar que está a ser aplicada uma função à lista de notas
        if re.search(r"::([^,]*)", lines[0]) != None:
            existe_func = True
            func = re.search(r"::([^,]*)", lines[0]).group(1)


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

                if existe_func:
                    # criar a lista de notas
                    notas = []
                    notas = re.search(r",\b\d+(?:,\d+)*(,)?", line).group(0).split(",")

                    # retirar valores nulos da lista de notas
                    notas.pop(0)
                    if (notas[notas.__len__() - 1] == ''):
                        notas.pop(notas.__len__() - 1)

                    if(func == "sum"):
                        res = sum(notas)

                        key = "Notas_" + func
                        dict[key] = res

                    if (func == "media"):
                        res = media(notas)

                        key = "Notas_" + func
                        dict[key] = res

                    if (func == "maior"):
                        res = maior(notas)

                        key = "Notas_" + func
                        dict[key] = res

                    if (func == "menor"):
                        res = menor(notas)

                        key = "Notas_" + func
                        dict[key] = res

                # se não estiver a ser aplicada uma função à lista de notas
                elif existe_func == False:

                    #criar a lista de notas
                    notas = []
                    notas = re.search(r",\b\d+(?:,\d+)*(,)?", line).group(0).split(",")

                    # retirar valores nulos da lista de notas
                    notas.pop(0)
                    if(notas[notas.__len__() - 1] == ''):
                        notas.pop(notas.__len__() - 1)

                    dict["Notas"] = notas

                # se estiver a ser aplicada uma função à lista de notas





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

#-----------------------------------------------------------------------------------------------------------------------

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

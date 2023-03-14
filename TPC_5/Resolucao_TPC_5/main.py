import os
import re

# ----------------------------------------------------------------------------------------------------------------------

def main():
    # construção da UI
    print(" ")
    print("--------------------------------- TPC 5 ---------------------------------")
    print(" ")
    print("Iniciando simulação de cabine telefónica")
    print("Insira comandos [LEVANTAR, POUSAR, MOEDA <lista de valores>, T=numero, ABORTAR] ")
    print(" ")
    print("-------------------------------------------------------------------------")
    print(" ")

    comand = ""

    while comand != "ABORTAR" or comand != "POUSAR":

        moedas = []
        num_telefone = ""

        comand = input("")  # input reservado para os comandos passados pelo utilizador

        if comand == "ABORTAR":
            print("")
            print("Abortado.......")
            print("Devolvendo moedas.......")
            print("")
            break

        elif comand == "POUSAR":
            print("")
            print("Abortado.......")
            print("Devolvendo moedas.......")
            print("")
            break


        else:
            print("Comando inválido!!!")
            print("")


if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------------------------
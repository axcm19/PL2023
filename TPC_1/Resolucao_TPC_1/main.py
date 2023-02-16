from doente import Doente
from listaDoentes import Lista_Doentes

def main():
    # abrir o ficheiro myheart.csv e criar o catalogo principal de doentes
    catalogo_doentes = Lista_Doentes()
    catalogo_doentes.parse("myheart.csv")

    # construção da UI
    saida = -1
    while saida != 0:
        print(" ")
        print("------------------ TPC 1 ------------------")
        print(" ")
        print("1 - Calcular a distribuição da doença por sexo")
        print("2 - Calcular a distribuição da doença por escalões etários")
        print("3 - Calcular a distribuição da doença por níveis de colesterol")
        print("4 - Imprimir na forma de uma tabela uma distribuição")
        print("5 - Imprimir o catalogo de doentes")
        print("0 - Saír")

        saida = int(input("Introduza a sua opcao-> "))

        if saida == 0:
            print("Saindo.......")

        elif saida == 1:
            # Calcular a distribuição da doença por sexo

            catalogo_doentes.calcula_dist_sexo()
            l = input("Prima enter para continuar")

        elif saida == 2:
            # Calcular a distribuição da doença por escalões etários

            print("")
            print(f"Maior idade = {catalogo_doentes.maior_idade()}")
            print(f"Menor idade = {catalogo_doentes.menor_idade()}")
            print("")

            catalogo_doentes.calcula_dist_etaria()

            l = input("Prima enter para continuar")

        elif saida == 3:
            # Calcular a distribuição da doença por níveis de colesterol


            l = input("Prima enter para continuar")

        elif saida == 4:
            # Imprimir na forma de uma tabela uma distribuição

            l = input("Prima enter para continuar")

        elif saida == 5:
            # Imprimir o catalogo de doentes

            for d in catalogo_doentes.lista_doentes:
                d.imprime()

            l = input("Prima enter para continuar")


        else:
            print("Opção inválida...")
            l = input("prima enter para continuar")

if __name__ == "__main__":
    main()

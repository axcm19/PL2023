from doente import Doente

class Lista_Doentes:

    def __init__(self):
        self.lista_doentes = []

    def parse(self, filename):

        try:
            f = open(filename)
            lines = f.readlines()

            idade = 0
            sexo = ""
            tensao = 0
            colestrol = 0
            batimento = 0
            temDoenca = 0  # 0 se não 1 se sim

            for line in lines:
                list = line.split(",")

                idade = list[0]
                sexo = list[1]
                tensao = list[2]
                colestrol = list[3]
                batimento = list[4]
                temDoenca = list[5]

                # cria um novo doente com base na informação retirada
                doente = Doente()
                doente.cria_doente(idade, sexo, tensao, colestrol, batimento, temDoenca)

                # adiciona o doente à lista
                self.lista_doentes.append(doente)

        finally:
            f.close()


    def calcula_dist_sexo(self):
        mascu_com_doenca = 0
        mascu_sem_doenca = 0

        fem_com_doenca = 0
        fem_sem_doenca = 0

        for doente in self.lista_doentes:
            if doente.sexo == "M" and int(doente.temDoenca) == 1:
                    mascu_com_doenca += 1

            if doente.sexo == "M" and int(doente.temDoenca) == 0:
                    mascu_sem_doenca += 1
            if doente.sexo == "F" and int(doente.temDoenca) == 1:
                    fem_com_doenca += 1
            if doente.sexo == "F" and int(doente.temDoenca) == 0:
                    fem_sem_doenca += 1

        print(" ")
        print(f"Doentes masculinos com doença = {mascu_com_doenca}")
        print(f"Doentes masculinos sem doença = {mascu_sem_doenca}")
        print(f"Doentes femininos com doença = {fem_com_doenca}")
        print(f"Doentes femininos sem doença = {fem_sem_doenca}")
        print(" ")

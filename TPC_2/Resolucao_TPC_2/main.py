

def main():

    print(" ")
    print("------------------------------ TPC 2 ------------------------------")
    print("Insira texto:")
    print("-------------------------------------------------------------------")
    print(" ")

    texto = input()
    soma = 0

    while True:

        for carater in texto:
            if carater.isdigit():
                soma += int(carater)


            if carater == "=":
                print(f"Soma total = {soma}")

        texto = input()







if __name__ == "__main__":
    main()

estoque_mercado = {}

#Função que mostra as opções
def menu():
    print("[1] Acessar o estoque", estoque_mercado)
    print("[2] Adicionar produtos")
    print("[3] Sair")

menu()
option = int(input("O que deseja fazer?:"))

while option != 0:
    if option == 1:
        print(estoque_mercado)
        break
    elif option == 2:
                    
    elif option == 3:
        print("Fechando sistema!")
        break

def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Não é possível dividir por zero."
    else:
        return n1 / n2

print("Olá, insira dois números para realizar a operação: ")

try:
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite o outro valor: "))
except ValueError:
    print("Valor inválido. Certifique-se de inserir números.")
    exit()

print("Agora, selecione uma das opções para fazer os devidos cálculos: ")
print(
    "1. Adição\n"
    "2. Subtração\n"
    "3. Multiplicação\n"
    "4. Divisão\n"
)

calculo = input("Escolha uma opção (1/2/3/4): ")

if calculo == "1":
    print("Resultado da adição:", adicao(n1, n2))
elif calculo == "2":
    print("Resultado da subtração:", subtracao(n1, n2))
elif calculo == "3":
    print("Resultado da multiplicação:", multiplicacao(n1, n2))
elif calculo == "4":
    print("Resultado da divisão:", divisao(n1, n2))
else:
    print("Opção inválida. Escolha uma das opções de 1 a 4.")

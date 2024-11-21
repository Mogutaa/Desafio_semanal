def soma (a,b):
    return a+b

def subtracao (a,b):
    return a-b

def multiplicacao (a,b):
    return a*b

def divisao (a,b):
    if b == 0:
        print("Não permitido divisão por zero")
    else:
        return a/b

operacoes = {"+":soma, "-":subtracao, "*":multiplicacao, "/":divisao}

while True:

    operacao = input("Digite a operacao desejada: \n+ \n- \n* \n/ \n")
    if operacao not in operacoes:
        print("Operação inválida")
        continue

    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
    except ValueError:
        print("Erro: Digite números válidos!")
        continue

    func = operacoes[operacao]
    resultado = func(num1, num2)  

    print("O resultado é: ", resultado)

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar == "n":
        print("Encerrando a calculadora. Até mais!")
        break
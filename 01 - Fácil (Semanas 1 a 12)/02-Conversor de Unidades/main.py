
#converte metros para quilometros
def metro_para_quilometros(metros):
    quilometros = metros / 1000
    return quilometros

#converte metros para centimetros
def metro_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

#converte metros para milimetros
def metro_para_milimetros(metros):
    milimetros = metros * 1000
    return milimetros

#converte quilometros para metros
def quilometros_para_metros(quilometros):
    metros = quilometros * 1000
    return metros

#converte quilometros para centimetros
def quilometros_para_centimetros(quilometros):
    centimetros = quilometros * 100000
    return centimetros

#converte quilometros para milimetros
def quilometros_para_milimetros(quilometros):
    milimetros = quilometros * 1000000
    return milimetros  

#converte centimetros para metros
def centimetros_para_metros(centimetros):
    metros = centimetros / 100
    return metros

#converte centimetros para quilometros
def centimetros_para_quilometros(centimetros):
    quilometros = centimetros / 100000
    return quilometros

#converte centimetros para milimetros
def centimetros_para_milimetros(centimetros):
    milimetros = centimetros * 10
    return milimetros

#converte milimetros para metros
def milimetros_para_metros(milimetros):
    metros = milimetros / 1000
    return metros

#converte milimetros para quilometros
def milimetros_para_quilometros(milimetros):
    quilometros = milimetros / 1000000
    return quilometros

#converte milimetros para centimetros
def milimetros_para_centimetros(milimetros):
    centimetros = milimetros / 10
    return centimetros

#dicionario de operacoes
operacoes = {
    "1": ("Metro para Quilometros", metro_para_quilometros ,"Metro(s)","Quilometro(s)"),
    "2": ("Metro para Centimetros",metro_para_centimetros,"Metro(s)","Centimetro(s)"),
    "3": ("Metro para Milimetros",metro_para_milimetros,"Metro(s)","Milimetro(s)"),
    "4": ("Quilometros para Metros",quilometros_para_metros,"Quilometro(s)","Metro(s)"),
    "5": ("Quilometros para Centimetros",quilometros_para_centimetros,"Quilometro(s)","Centimetro(s)"),
    "6": ("Quilometros_para_centimetros",quilometros_para_milimetros,"Quilometro(s)","Milimetro(s)"),
    "7": ("Centimetros para Metros",centimetros_para_metros,"Centimetro(s)","Metro(s)"),
    "8": ("Centimetros para Quilometros",centimetros_para_quilometros,"Centimetro(s)","Quilometro(s)"),
    "9": ("Centimetros para Milimetros",centimetros_para_milimetros,"Centimetro(s)","Milimetro(s)"),
    "10": ("Milimetros para Metros",milimetros_para_metros,"Milimetro(s)","Metro(s)"),
    "11": ("Milimetros para Quilometros",milimetros_para_quilometros,"Milimetro(s)","Quilometro(s)"),
    "12": ("Milimetros para Centimetros",milimetros_para_centimetros,"Milimetro(s)","Centimetro(s)"),
}

#menu 
while True:

    
    print("Selecione a operação desejada:")
    for operacao in operacoes:
        print(f"{operacao}: {operacoes[operacao][0]}")

    operacao = input("Operação: ")    
    if operacao not in operacoes:
        print("Operação inválida.")
        continue
    elif operacao in operacoes:
        print(f"Operação selecionada: {operacoes[operacao][0]}")
        

    try:
        valor = float(input("Digite o valor: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico.")

    func = operacoes[operacao][1]
    resultado = func(valor)

    print(valor, operacoes[operacao][2], "Convertidos em", operacoes[operacao][3], "é: ", resultado, 
          operacoes[operacao][3])

    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != "s":
        print("Encerrando o programa.")
        break
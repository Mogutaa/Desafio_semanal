
# Loop Principal
while True:

    # Entrada de Dados
    print("Bem vindo ao contador de palavras e caracteres")
    texto = input("Digite um texto para contar as palavras: ")

    # Contar o Número de Palavras
    palavras = texto.split()
    numero_de_palavras = len(palavras)
    # Contar os Caracteres
    numero_de_caracteres = len(texto.replace(" ", ""))

    # Palavras únicas
    palavras_unicas = set(palavras)
    numero_de_palavras_unicas = len(palavras_unicas)

    # Exibir os Resultados
    print(f"Numero de palavras: {numero_de_palavras}")
    print(f"Numero de caracteres (sem espacos): {numero_de_caracteres}")
    print(f"Numero de palavras unicas: {numero_de_palavras_unicas}")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        break
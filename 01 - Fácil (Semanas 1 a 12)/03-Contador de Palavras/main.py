from database import *

def main():
# Loop Principal
    while True:
        # Entrada de Dados
        print("=======Bem vindo ao contador de palavras e caracteres======= \n")
        texto = input("Digite um texto: ")
        if not texto.strip():
            print("Por favor, insira um texto válido!")
            continue

        exibir_resultados(texto)

        continuar = input("\nDeseja continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Obrigado por usar o contador de palavras. Até a próxima!")
            break

if __name__ == "__main__":
     main()
    
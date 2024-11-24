from database import *


#selecao de menus
menus = {
    "1": ("Calculadora de Comprimento",conversoes_comprimento), 
    "2": ("Calculadora de Temperatura",conversoes_temperatura), 
    "3": ("Calculadora de Volume",conversoes_volume)
    }

#exibir menus
def exibir_menu():
    for chave, valor in menus.items():
        print(f"{chave} - {valor[0]}")

#exibir submenus
def exibir_submenu(conversoes):
    for chave, (descricao, _, unidade_entrada, unidade_saida) in conversoes.items():
        print(f"{chave} - {descricao} ({unidade_entrada} -> {unidade_saida})")


#realizar conversoes
def realizar_conversoes(funcao_conversao,unidade_entrada,unidade_saida):
    try:
        valor = float(input("Digite o valor a ser convertido: "))
        resultado = funcao_conversao(valor)
        print(f"{valor} {unidade_entrada} equivale a {resultado} {unidade_saida}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

def main():
   while True: 
    exibir_menu()
    opcao_menu = input("Escolha uma opcao: ")
    if opcao_menu not in menus:
        print("Opcao invalida. Por favor, escolha uma opcao valida.")
        continue
    
    menu_selecionado = menus[opcao_menu]
    nome_menu = menu_selecionado[0]
    sub_menu = menu_selecionado[1]

    print(f"Voce escolheu o menu {nome_menu}")
    exibir_submenu(sub_menu)

    opcao_conversao = input("Escolha uma opcao: ")
    if opcao_conversao not in sub_menu:
        print("Opcao invalida. Por favor, escolha uma opcao valida.")
        continue
    descricao, funcao_conversao, unidade_entrada, unidade_saida = sub_menu[opcao_conversao]
    print(f"Voce escolheu a opcao {descricao}")
    realizar_conversoes(funcao_conversao,unidade_entrada,unidade_saida)

    continuar = input("Deseja realizar outra conversao? (S/N): ").lower()
    if continuar != "s":
        break
    

if __name__ == "__main__":
    main()
    
        


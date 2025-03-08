#importando ultilidades 
from utilidades import limpar_Tela
import time

#Função Menu
def Menu():
    print(f'{'='*20} MENU {'='*20}')
    menu =[
        '(1) - verficar integridade das informações',
        '(2) - Exibir amostra dos dados',
        '(3) - Verificar estatísticas descritivas',
        '(4) - Sair'
         ]
    for item in menu:
        print(item)

# Função escolha
def escolha():
    Menu()
    opcoes = {
        1: 'verificar integridade',
        2: 'Exibir amostra dos dados',
        3: 'Verificar estatísticas descritivas',
        4: 'Sair'
    }
    while True:
        try:
            print("="*46)
            opcao = int(input("Digite somente o número da seleção: "))
            limpar_Tela()
            
            if opcao in opcoes: 
                acao = opcoes[opcao]
                print(f"Você escolheu: {acao}")
                if opcao == 4:
                    print("Saindo...")
                    break
            else:
                print("="*46)
                print("Ação não permitida, tente novamente.")
                print("="*46)
                time.sleep(3.0)
                limpar_Tela()
                escolha()  
        except ValueError:
            print("="*46)
            print("Somente Números inteiros são aceitos!!")
            print("="*46)
            time.sleep(3.0)
            limpar_Tela()
            escolha()
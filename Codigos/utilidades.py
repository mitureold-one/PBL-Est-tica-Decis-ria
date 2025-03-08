import os

#função para limpar a tela 
def limpar_Tela():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        clear_output()
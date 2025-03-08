#importando bibliotecas
import pandas as pd
import os


#criando um caminho flexivel para os arquivos serem carregados no programa(importante para compartilhar o codigo)
pasta_dados = os.path.join(os.getcwd(), "dados") 

#importando planilhas do excel 
Produtos = pd.read_excel(os.path.join(pasta_dados, 'Cadastro Produtos.xlsx'))#produtos
Lojas =  pd.read_excel(os.path.join(pasta_dados, 'Cadastro Lojas.xlsx'))#lojas
Clientes =  pd.read_excel(os.path.join(pasta_dados, 'Cadastro Clientes.xlsx'))#clientes
Localidades=  pd.read_excel(os.path.join(pasta_dados, 'Cadastro Localidades.xlsx'))#localidas
Devoluções =  pd.read_excel(os.path.join(pasta_dados, 'Base Devoluções.xlsx'))#devoluções
Vendas_20=  pd.read_excel(os.path.join(pasta_dados, 'Base Vendas - 2020.xlsx'))#vendas 2020
Vendas_21 =  pd.read_excel(os.path.join(pasta_dados, 'Base Vendas - 2021.xlsx'))#vendas 2021
Vendas_22 = pd.read_excel(os.path.join(pasta_dados, 'Base Vendas - 2022.xlsx'))#vendas 2022
Vendas = pd.concat([Vendas_20, Vendas_21, Vendas_22])#vendas globais

#vendo as informaçoes 

#Função para verificar valores nulos nas planilhas
def colunas_vazias (Planilha):
    informacoes = Planilha.isnull().mean()*100
    colunas_com_nulos = informacoes[informacoes > 0]  

    if colunas_com_nulos.empty:
        print(f'A planilha não possui informações vazias.')
    else:
        print('A planilha possui valores nulos nas seguintes colunas:')
        print(colunas_com_nulos)
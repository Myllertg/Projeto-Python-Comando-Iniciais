#%%
import requests         # Biblioteca usada para fazer requisições na internet (consumir APIs)
import json             # Biblioteca usada para trabalhar com dados no formato JSON (muito comum em APIs)
from tqdm import tqdm   # Biblioteca para exibir uma barra de progresso no loop
import pandas as pd     # Biblioteca para manipulação de dados em formato de tabela

#%%

# Lista de CEPs que serão consultados na API
ceps = [
    "35020220",
    "35270000",
    "58038200"
]

# URL da API ViaCEP
# {cep} é um "placeholder", ou seja, será substituído por cada CEP da lista durante o loop
url = "https://viacep.com.br/ws/{cep}/json/"

# Lista vazia que irá armazenar os dados retornados pela API
dados = []

# Loop que percorre cada CEP da lista
# tqdm adiciona uma barra de progresso para acompanhar a execução
for i in tqdm(ceps): 
    # Faz a requisição para a API, substituindo {cep} pelo valor atual da lista
    resposta = requests.get(url.format(cep=i))

    # Verifica se a requisição foi bem-sucedida (status code 200 = sucesso)
    if resposta.status_code == 200:
        # Converte a resposta para JSON (dicionário Python)
        # e adiciona na lista "dados"
        dados.append(resposta.json())  

# Exibe os dados coletados (apenas para conferência)
dados 

#%%

# Converte a lista de dicionários em um DataFrame (tabela)
dataset = pd.DataFrame(dados)

# Salva os dados em um arquivo CSV
# sep=";" define que o separador será ponto e vírgula (padrão comum no Brasil)
dataset.to_csv("ceps.csv", sep=";")

#%%

# Abre (ou cria) um arquivo JSON para escrita
# "w" = modo de escrita
# encoding='utf-8' garante suporte a acentos
with open("ceps.json", "w", encoding='utf-8') as open_file:
    
    # Salva os dados no formato JSON dentro do arquivo
    # ensure_ascii=False mantém caracteres especiais (acentos)
    # indent=4 deixa o arquivo formatado e mais fácil de ler
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

#%%
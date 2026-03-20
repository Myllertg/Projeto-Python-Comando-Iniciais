import streamlit as st  # Biblioteca usada para criar interfaces web de forma simples 
import pandas as pd     # Biblioteca para manipulação e organização de dados em formato de tabela
import requests         # Biblioteca para fazer requisições na internet (consumir APIs)

# URL da API ViaCEP.
# O {cep} funciona como um espaço reservado que será substituído pelo CEP digitado pelo usuário
URL = "https://viacep.com.br/ws/{cep}/json/"

# Cria um campo de texto na tela para o usuário digitar o CEP
# O valor digitado será armazenado na variável "cep"
cep = st.text_input("Busque seu cep")

# Verifica se o usuário digitou alguma coisa (se não está vazio)
if cep != "":
    try:
        # Faz uma requisição para a API, substituindo {cep} pelo valor digitado
        # Exemplo: https://viacep.com.br/ws/01001000/json/
        resp = requests.get(URL.format(cep=cep))

        # Converte a resposta da API (JSON) em um formato de tabela (DataFrame)
        # O [ ] é usado para transformar o dicionário em uma lista (necessário para criar a tabela)
        data = pd.DataFrame([resp.json()])

        # Exibe os dados na tela em formato de tabela
        # hide_index=True remove a coluna de índice (deixa mais limpo visualmente)
        st.dataframe(data, hide_index=True)

    except Exception as err:
        # Caso ocorra qualquer erro (ex: CEP inválido, falha na conexão, etc.)
        # Exibe uma mensagem de erro na tela para o usuário
        st.error("Entre com um cep válido!")

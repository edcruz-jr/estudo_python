"""
Funcionalidades de Series:
1-Armazenamento de Dados Unidimensionais;
2-Operações vetorizadas;
3-Focado em Dados Estruturados;
"""

import pandas as pd #Importando a biblioteca pandas

print(pd.__version__)

#1-Dados dos times e suas quantidades de títulos
dados = {
    "Real Madrid":34,
    "Barcelona":26,
    "Liverpool":19,
    "Juventus":36,
    "Bayern Munich":30
}

#2-Criando uma Series a partir de um dicionário
series_time = pd.Series(dados)

print(series_time)
print(type(series_time)) #Verificando o tipo

#3-Selecionar times por índice
print(series_time["Real Madrid"])
print(series_time.iloc[2])

#4-Selecionando por fatiamento
print(f"\n{series_time["Barcelona":"Juventus"]}") #Fatiamento é inclusivo

#5-Selecionar por condição
print(f"\n{series_time[series_time>=36]}") #Selecionando os times com títulos maiores ou iguais a 36
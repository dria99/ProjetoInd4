# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1COgCtlDgB_Jgxtx9uz8CemQvsaYLGP5k
"""

import pandas as pd
import matplotlib.pyplot as plt

# Dados
data = {
    'Dia': ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'],
    'Horas Trabalhadas': [6, 7, 8, 6, 7, 5, 4],
    'Bugs Corrigidos': [3, 2, 1, 4, 3, 2, 1],
    'Tarefas Concluidas': [5, 4, 6, 4, 5, 3, 2]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Cálculos
total_horas = df['Horas Trabalhadas'].sum()
media_horas = df['Horas Trabalhadas'].mean()
total_bugs = df['Bugs Corrigidos'].sum()
media_bugs = df['Bugs Corrigidos'].mean()
total_tarefas = df['Tarefas Concluidas'].sum()
media_tarefas = df['Tarefas Concluidas'].mean()
produtividade = total_tarefas / total_horas

# Relatório
print(f'Total de Horas Trabalhadas: {total_horas:.2f}')
print(f'Média Diária de Horas Trabalhadas: {media_horas:.2f}')
print(f'Total de Bugs Corrigidos: {total_bugs:.2f}')
print(f'Média Diária de Bugs Corrigidos: {media_bugs:.2f}')
print(f'Total de Tarefas Concluídas: {total_tarefas:.2f}')
print(f'Média Diária de Tarefas Concluídas: {media_tarefas:.2f}')
print(f'Produtividade Diária (Tarefas Concluídas por Hora): {produtividade:.2f}')

# Gráficos
df.set_index('Dia').plot(kind='bar', subplots=True, layout=(2,2), legend=False)
plt.tight_layout()
plt.show()
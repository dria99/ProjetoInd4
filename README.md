Sistema de Relatório de Progresso Diário
Descrição
Este sistema tem como finalidade gerar um relatório de progresso diário para mostrar o quão produtivo está sendo o trabalho dos funcionários. O relatório inclui os seguintes itens:
Total de Horas Trabalhadas
Média Diária de Horas Trabalhadas
Total de Bugs Corrigidos
Média Diária de Bugs Corrigidos
Total de Tarefas Concluídas
Média Diária de Tarefas Concluídas
Produtividade Diária (Tarefas Concluídas por Hora)
Este relatório tem o objetivo de demonstrar a importância da análise dos dados de um projeto de desenvolvimento de software ao longo de uma semana. Os dados fornecidos permitirão ao proprietário da equipe de desenvolvimento obter insights sobre o progresso do projeto, identificar possíveis áreas de melhoria e tomar decisões informadas para garantir o sucesso do projeto.
Como usar
Faça o download do projeto.
Execute o script principal.
Verifique o relatório gerado.
Contribuindo
Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar uma solicitação pull.
Licença
Este projeto está licenciado sob a licença MIT.




Sistema de Relatório de Progresso Diário

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






Total de Horas Trabalhadas: 43.00
Média Diária de Horas Trabalhadas: 6.14
Total de Bugs Corrigidos: 16.00
Média Diária de Bugs Corrigidos: 2.29
Total de Tarefas Concluídas: 29.00
Média Diária de Tarefas Concluídas: 4.14
Produtividade Diária (Tarefas Concluídas por Hora): 0.67







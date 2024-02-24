# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

gasolina_df = pd.read_csv('gasolina.csv')

with sns.axes_style ('whitegrid'):
  grafico = sns.FacetGrid(data = gasolina_df, palette = 'pastel')
  grafico.map(sns.lineplot, 'dia', 'venda')
  grafico.map(plt.fill_between, 'dia', 'venda', alpha = 0.2)
  grafico.set(title = 'Preço da gasolina', xlabel = 'dia',ylabel ='venda')
  grafico.fig.set_size_inches(w=15/2.54, h= 7/2.54)
  plt.savefig("gasolina.png")
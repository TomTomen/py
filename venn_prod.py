# -*- coding: utf-8 -*-
"""Venn_Prod.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RYYjERMh5hnLP25_pR-fxkYKJiWE0oD8
"""

!wget https://github.com/TomTomen/py/raw/refs/heads/main/Common%20genes%204%20strains%20Pseudomonas.xlsx

!wget https://github.com/TomTomen/py/raw/refs/heads/main/Gene%20presence%20absence.xlsx

import pandas as pd
# Чтение и преобразование таблицы в DataFrame с отбором значимых данных
df_cleaned = pd.read_excel("/content/Gene presence absence.xlsx", sheet_name='gene_presence_absence')

# Удалим строки, содержащие NaN в ключевых столбцах, и переименуем заголовки
#df_cleaned = df_cleaned.drop(columns=['Unnamed: 0'])
#df_cleaned = df_cleaned.rename(columns={'Unnamed: 1': 'Strain'})

# Посмотрим на преобразованные данные
df_cleaned.head(10)

df_cleaned[df_cleaned['P_PLB05'] != 0][['Gene/Protein', 'P_PLB05']]
#set(df_cleaned[df_cleaned['P_PLB05'] != 0]['Gene/Protein'])

genes_PLB05 = 1537
genes_P_rhyz = 2934
genes_P_oryz = 340
genes_P_psych = 956

# Overlap data
overlap_PLB05_P_rhyz = 1736
overlap_PLB05_P_oryz = 2907
overlap_PLB05_P_psych = 3055
overlap_P_rhyz_P_oryz = 1863
overlap_P_rhyz_P_psych = 1832
overlap_P_oryz_P_psych = 4196

genes_PLB05_s = set(df_cleaned[df_cleaned['P_PLB05'] != 0]['Gene/Protein'])
genes_P_oryz_s = set(df_cleaned[df_cleaned['P_oryz'] != 0]['Gene/Protein'])
genes_P_psych_s = set(df_cleaned[df_cleaned['P_psych'] != 0]['Gene/Protein'])
genes_P_rhyz_s = set(df_cleaned[df_cleaned['P_rhyz'] != 0]['Gene/Protein'])

!pip install venn
from venn import venn,generate_petal_labels,draw_venn,generate_colors
import matplotlib.pyplot as plt

venn_data = {
    'PLB05': genes_PLB05_s,
    'P_ory': genes_P_oryz_s,
    'P_psych': genes_P_psych_s,
    'P_rhyz': genes_P_rhyz_s,
}
petal_labels = generate_petal_labels(venn_data.values(), fmt="{size}")
print("Изначальные метки для лепестков:", petal_labels)

filtered_labels = {}
for logic, value in list(petal_labels.items()):
    if logic.count("1") > 2:
        filtered_labels[logic] = petal_labels.pop(logic)
filtered_labels

for logic in list(filtered_labels.keys()):
    del filtered_labels[logic]

plt.figure(figsize=(10, 8))
draw_venn(
    petal_labels=petal_labels,
    dataset_labels=venn_data.keys(),
    hint_hidden=False,
    colors=generate_colors(n_colors=4),
    figsize=(8, 8),
    fontsize=14,
    legend_loc="best",
    ax=None
)
plt.title("Venn Diagram of Gene Overlaps")
plt.show()

venn_data = {
    'PLB05': genes_PLB05_s,
    'P_ory': genes_P_oryz_s,
    'P_psych': genes_P_psych_s,
    'P_rhyz': genes_P_rhyz_s,
}

#custom_petal_labels = {}
#names = list(venn_data.keys())
#for logic in list(petal_labels.keys()):
#    index = logic.count('1')  # Определяем количество пересечений
#    if index > 0:
#        indices = [i for i, char in enumerate(logic) if char == '1']
#        involved_names = [names[i] for i in indices]
#        name = "_".join(involved_names)
#        custom_petal_labels[name] = f"{petal_labels[logic]}"



petal_labels = {
  '1000': str(genes_PLB05),
  '0100': str(genes_P_oryz),
  '0010': str(genes_P_psych),
  '0001': str(genes_P_rhyz),
  '1100': str(overlap_PLB05_P_oryz),
  '1010': str(overlap_PLB05_P_psych),
  '1001': str(overlap_PLB05_P_rhyz),
  '0110': str(overlap_P_oryz_P_psych),
  '0101': str(overlap_P_rhyz_P_oryz),
  '0011': str(overlap_P_rhyz_P_psych),
  '1110': str(0),
  '1101': str(0),
  '1011': str(0),
  '0111': str(0),
  '1111': str(0)
}

significance_filter = lambda value: value if int(value) != 0 else ""
petal_labels = {
    logic: significance_filter(value)
    for logic, value in petal_labels.items()
}


plt.figure(figsize=(10, 8))
draw_venn(
    petal_labels=petal_labels,
    dataset_labels=venn_data.keys(),
    hint_hidden=False,
    colors=generate_colors(n_colors=4),
    figsize=(8, 8),
    fontsize=14,
    legend_loc="best",
    ax=None
)
plt.title("Venn Diagram of Gene Overlaps")
plt.show()

petal_labels = {
  '1000': str(genes_PLB05),
  '0100': str(genes_P_oryz),
  '0010': str(genes_P_psych),
  '0001': str(genes_P_rhyz),
  '1100': str(overlap_PLB05_P_oryz),
  '1010': str(overlap_PLB05_P_psych),
  '1001': str(overlap_PLB05_P_rhyz),
  '0110': str(overlap_P_oryz_P_psych),
  '0101': str(overlap_P_rhyz_P_oryz),
  '0011': str(overlap_P_rhyz_P_psych),
  '1110': str(0),
  '1101': str(0),
  '1011': str(0),
  '0111': str(0),
  '1111': str(0)
}
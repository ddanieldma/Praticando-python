import numpy as np
import pandas as pd

print("##### Criando DATAFRAMES #####")

indices = ["The Pacific", "Black Mirror", "CSI", "NCIS", "Lost"]
colunas = ["Nota", "Temporadas", "Episódios"]
dados = [[8.3, 1, 10], [8.3, 6, 27], [7.7, 15, 337], [6.9, 14, 458], [8.3, 6, 121]]
df = pd.DataFrame(dados, index=indices, columns=colunas)

print(df, end="\n\n")

#=========================================================================
print("\n\n##### Seleção #####")
print("Notas: ")
print(df["Nota"], end="\n\n")
print(df[["Temporadas", "Episódios"]], end="\n\n")

#=========================================================================
print("\n\n##### Loc ILOC #####")
print("Lost: ")
# localizador por rotulo
print(df.loc["Lost"], end="\n\n") 
# localizando primeiro índice
print(df.iloc[0], end="\n\n") 

#=========================================================================
print("\n\n##### Seleção combinada #####")
# buscando uma lista de indices
print(df.loc[["The Pacific", "NCIS"], "Temporadas"], end="\n\n")
# buscando tempradas e nota para todos os índices
print(df.loc[:, ["Temporadas", "Nota"]], end="\n\n")

#=========================================================================
# print(type(df.loc[:, [""]]))

print(df.columns)
print(type(df.columns))
print(df.columns.values)
print(type(df.columns.values))

print(df.index)
print(type(df.index))
print(df.index.values)
print(type(df.index.values))

# criando nova coluna no df
df["Coluna extra"] = df["Nota"]
print(df, end ="\n\n")

# retirando coluna
df.drop("Coluna extra", axis=1, inplace=True)
print(df, end="\n\n")

# retirando por indice
df.drop("Lost", axis=0, inplace=True)
print(df, end="\n\n")

print(df.shape)# (4, 3)

#=========================================================================
print("\n\n##### SELEÇÃO CONDICIONAL #####")

print(df[df["Nota"] > 8])
# coloca True em todos os dados do df maiores que 3
print(df>3)
print(df[df>3]) # os valores menores que 3 fica como NaN

#=========================================================================
print("\n\n##### SELEÇÃO CONDICIONAL + MÚLTIPLA #####")

# temporadas das séries com nota acima de 8
print(df[df["Nota"] > 8]["Temporadas"]) 
# temporadas e episódios das séries com nota acima de 8
print(df[df["Nota"] > 8][["Temporadas", "Episódios"]])

print(df[(df["Nota"] > 8) & (df["Temporadas"]>3)]) 

#=========================================================================
print("\n\n##### MULTI-INDEX #####")

plataforma = ["HBO", "HBO", "Netflix", "Netflix"]
lancamento = [2020, 2021, 2020, 2021]
indices = pd.MultiIndex.from_arrays([plataforma, lancamento], names=("Plataforma", "Lançamento"))
print("\n\nIndices: ")
print(indices)

print("\nSem Índice: ")
df.reset_index(inplace=True)
print(df)

print("\nRenomear Índice: ")
df.rename(columns={"index":"Nome"}, inplace=True)
print(df)

print("\nConfigurar Índice: ")
df.set_index(indices, inplace=True)
print(df)

print("\nSeleção Multi-Index: ")
print(df.loc["HBO"].loc[2021])

print("\nCross Selection 1: ")
print(df.xs("HBO"))

print("\nCross Selection 3: ")
# Selecionando índice da direita pra esquerda>
print(df.xs(2020, level="Lançamento"))

#=========================================================================
print("\n\n##### OPERAÇÕES #####")

print("Unique ", df["Nota"].unique())# notas únicas
print("Nunique ", df["Nota"].unique())
print("Count ", df["Nota"].count())

df.at[("HBO", 2020), "Nota"]

#=========================================================================
print("\n\n##### OPERAÇÕES AGREGADAS #####")

print("Min: ", df["Nota"].min())
print("Max: ", df["Nota"].max())
print("Median: ", df["Nota"].median())
print("Var: ", df["Nota"].var())

#=========================================================================
print("\n\n##### DROP & FILL #####")

indices = ["Aluno 1", "Aluno 2", "Aluno 3"]
colunas = ["Nome", "Altura", "Sono Médio"]
dados = [["Giovanna Grossi", 173, 7], ["Uriel Liann", 180, np.nan], ["Pedro Tokar", 182, 6]]
alunos = pd.DataFrame(dados, index=indices, columns=colunas)
print(alunos)

print("Is Null: ", alunos.isnull(), sep="\n")
print("\nIs Null: ", alunos["Sono Médio"].isnull(), sep="\n")

print("Null: ", alunos[alunos.isnull()], sep="\n")
print("\nNull: ", alunos[alunos["Sono Médio"].isnull()], sep="\n")

alunos.dropna(thresh=2, inplace=True)# se a linha tem mais que 2 NaN, dropa a linha
print(alunos)
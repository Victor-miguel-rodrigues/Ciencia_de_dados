import pandas as pd
import numpy as np



df_analise_mes_1 = pd.read_csv('./csvs/ecommerce_2025_month_1.csv')
#df_analise_mes_1.info()
display(df_analise_mes_1)

# Tratamento de tipos de dados
df_analise_mes_1['price'] =  pd.to_numeric(df_analise_mes_1['price'] , errors='coerce')
df_analise_mes_1['order_date'] =  pd.to_datetime( df_analise_mes_1['order_date'])
display(df_analise_mes_1.info())

#tratamento valores nulos
df_price_null = df_analise_mes_1[df_analise_mes_1['price'].isnull()]

#df_analise = pd.to_numeric(df_analise_mes_1[df_analise_mes_1['delivery_days'].astype(int).notnull], errors='coerce')

# transformando dias em numero inteiro
df_delivery = df_analise_mes_1[df_analise_mes_1['delivery_days'].notnull()]
df_analise = pd.to_numeric(df_delivery['delivery_days'], downcast='integer')



import pandas as pd
import numpy as np


try: 
    arquivo = pd.read_csv("ecommerce_2024.csv", encoding="utf-8", sep=",", low_memory=False)
    # so retorna oq voltou 
    returned = arquivo[arquivo['returned'] == "Yes"]
    #retorna oq não voltou
    notReturned = arquivo[arquivo['returned'] == "No"]
    display(notReturned)
    display(returned)

except Exception as error:
    print(error)
 
  # coisa retiradas do projetoooooooo
    #price = arquivo['price']
    #quantity = arquivo['quantity']
    #faturamento = price * quantity

try:
    # faturamento do ano
    value = np.sum(arquivo['price'] *  arquivo['quantity'])
    display(value)
except Exception as error:
    print(error)



# inspeção

#quantas linhas você deseja ver
display(arquivo.head(5))

# final da base de dados
display(arquivo.tail(5))

# amostra - pega 15 linha da base de dados aleatoriamente
display(arquivo.sample(15))


# mostra as linhas e colunas 
print(f"Linha :{arquivo.shape[0]}")
print(f"Coluna :{arquivo.shape[1]}")

# transforma em lista
print(arquivo.columns)
print(list(arquivo.columns))


display(arquivo.info())
display(arquivo.describe())


# tratamento de dados

# colunas
# 1 coluna
#display(arquivo['delivery_days'])
# uma lista de colunas
#display(arquivo[['delivery_days','region']])

display(arquivo[['payment_method','delivery_days']])

# valores nulos

# tipos de dados

# valores duplicados



# remove valor da planilha
#df_analise = arquivo.drop(columns='total_value')
#display(df_analise)

# tratamento simples de valores nulos

# valores nulos
df_analise = df_analise.dropna()
#display(df_analise)

# modificar listas vazias
# df_analise['Oq vai ser modificado'] = df_analise['Oq vai ser modificado'].fillna("oq vai ser utilizado")
# preencher todos os valores vazios
df_analise1 = df_analise['returned'].fillna("colocar aqui oq vai ser usado para  preencher")

# tipos de dados
df_analise['order_date'] = pd.to_datetime(df_analise['order_date'], format="%Y-%m-%d")


df_analise.info()

# Padronização 
df_analise['payment_method'] = df_analise['payment_method'].str.strip()
df_analise['payment_method'] = df_analise['payment_method'].str.title()
df_analise['product_name'] = df_analise['product_name'].str.title()
# valores duplicados

display(df_analise)

import pandas as pd
import numpy as np

try:
    archive = pd.read_csv("ecoomerce.csv")
    art = archive[archive["delivery_time_days"] < 8]
    print("\nTempo de entrega ate 7 dias")
    display(art.sort_values(by='delivery_time_days',ascending=True))
    

    tardio = archive[archive["delivery_time_days"] > 7]
    print("\ntempo de entrega maior que 7 dias")
    display(tardio.sort_values(["delivery_time_days"], ascending=False))
    
    if(archive[archive["review_score"] < 3].all):
        print("Score ruim abaixo de 3 estrelas")
        display(archive[archive["review_score"] <= 2])

except Exception as error:
    print(f"ERRor ?={error}")



import matplotlib.pyplot as plt

plt.title("Grafico de visibilidade de vendas")
a = [1,2,3,4]
b = [0,-3,5,6]
z = [2,-5,3,2]
j = [12,16,12,11]

plt.plot(a,b)
plt.plot(a,z)
plt.plot(a,j)
plt.show()


# modificar as linhas   '-', '--', '-.', ':'

plt.plot(a,b, ls = "-.",  color="#28BBFF")

# Marcadores0
plt.plot(a,b, ls = "-.",  color="#28BBFF", marker="o")
plt.plot(a,z, ls = "-.",  color="#141414", marker="v",linewidth=3)

plt.style.use("bmh")
plt.title("Meu grafico")
plt.plot(a,b, color="#10FF10" , label = "Mes de janeiro", linewidth=5)
plt.legend()
plt.xlabel("Tempo")
plt.ylabel("Valor")
plt.show()


figura = plt.figure(figsize=(20,6))
figura.suptitle("Meus graficos")

figura.add_subplot(231)
plt.plot(a,z, ls="-", label="Valores",linewidth=2)
plt.title("Grafico_1")
plt.legend()

figura.add_subplot(232)
plt.plot(b,z, ls="-", label="Tempo",linewidth=2)
plt.title("Grafico_2")
plt.legend()

figura.add_subplot(233)
plt.plot(a,b, ls="-", label="Decisao",linewidth=2)
plt.title("Grafico_3")
plt.legend()

plt.show()


# grafico de pontos

plt.scatter(a,z, marker="^",color="r")
plt.title("Grafico de pontos")
plt.show()


plt.style.use("ggplot")
plt.bar(a,z, color='b', label="Valores")
plt.title("Grafico de barras")
plt.legend()
plt.ylabel("Valores")
plt.show()
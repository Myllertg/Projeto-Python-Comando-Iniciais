# %%

lista = [2,132, "theo",["ds","de","da"], True]

lista [2]

#%%

dados_teo={"Sobrenome":"Shimabukuro",
           "nome":"theo",
            "filhos":True,
            "formação":["estatistica","big datascience"],
             }

print(dados_teo)


# %%
dados_teo ["nome"]


# %%
dados_teo["Estado Civil"] = "casado"


#%%


print ("Chaves:", dados_teo.keys())
print(dados_teo.values())
print("items:", dados_teo.items())


# %%

for i in dados_teo:
    print(i,"->", dados_teo[i])


# %%

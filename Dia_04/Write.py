#%%

txt = "Meu novo arquivo!"

nome_arquivo = "historia_02.txt"

with open (nome_arquivo, mode = "w") as open_files:
    open_files.write(txt)


# %%

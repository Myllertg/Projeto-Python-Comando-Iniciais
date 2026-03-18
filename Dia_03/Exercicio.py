#%%
lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = input ("Digite um nomero", ) 
numero = int (numero)

i = 0
count = 0

while i < len (lista):

    if lista [i] == numero:
        count += 1
    i += 1

print(count)
    



# %%

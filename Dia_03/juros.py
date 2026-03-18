#%%

def juros_compostos(aporte: int, taxa:float, anos:int) :
    """ testes 
    texto para explicar a função
    
    """
    return aporte * (1+taxa) ** anos


#%%

juros_compostos(taxa=0.13, anos = 5, aporte =1000)
# %%

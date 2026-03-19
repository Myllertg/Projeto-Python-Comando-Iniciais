## Importa a biblioteca "random", que permite gerar números aleatórios (como um sorteio)
import random



# Função responsável por pedir um número ao usuário
# Ela continuará pedindo até que o valor digitado seja válido
def get_input():
 while True:  # Cria um loop infinito que só será interrompido quando um valor correto for inserido
        try:
            # Solicita que o usuário digite um número e tenta convertê-lo para inteiro
            numero_usuario = int(input("Entre com o número: "))
        except ValueError: # Caso o usuário digite algo que não seja um número inteiro (ex: letras), exibe erro e pede novamente
            print("Valor inválido!")
            continue  # Retorna ao início do loop para tentar novamente

        # Verifica se o número está dentro do intervalo permitido (de 1 a 15)
        if 1 <= numero_usuario <= 15:         
           return numero_usuario  # Se estiver correto, a função retorna o número digitado e encerra
           
       
        # Caso o número esteja fora do intervalo permitido, orienta o usuário e repete o processo
        print("Digite um número entre 1 e 15!")



# Função que compara o número digitado pelo usuário com o número sorteado
def check_numbers (numero_sorteio, numero_usuario):

    # Se o número digitado for exatamente igual ao número sorteado
    if numero_usuario == numero_sorteio:
        print("Parabéns!")
        return True  # Retorna verdadeiro indicando que o usuário acertou

    # Se o número digitado for maior que o número sorteado
    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor!")
        return False  # Retorna falso indicando que o usuário errou

    # Se o número digitado for menor que o número sorteado
    else:
        print("Número muito baixo. Tente um número maior!")
        return False  # Retorna falso indicando que o usuário errou



# Aqui é feito o sorteio de um número aleatório entre 1 e 15
numero_sorteio = random.randint(1,15)


# Inicia um laço de repetição que dará ao usuário até 3 tentativas
for i in range(3):
   
   # Chama a função que solicita um número ao usuário e garante que ele seja válido
    numero_usuario=get_input()
    
    # Verifica se o número digitado é igual ao número sorteado
    # Se for igual, a função retorna True e o programa encerra o loop
    if check_numbers (numero_sorteio=numero_sorteio, numero_usuario=numero_usuario):
     break

    
# Caso o usuário utilize todas as 3 tentativas sem acertar, este bloco será executado
else: 
    print("Suas tentativas acabaram!! O numero era:  ", numero_sorteio)

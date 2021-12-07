#Chute o número
'''
Escreva um programa que, ao iniciar gere um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatóriamente gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

1. Quais os dados de entradas necessários?
R: Valor aleatório de 1 a 10; Chute do usuário

2. O que devo fazer com estes dados?
R: Eu devo comparar o chute do usuário com o valor aleatório que foi gerado no início do programa e dizer se o chute foi maior, menor ou igual ao valor que foi gerado no programa.

3. Quais são as restrições deste problema ?
R: Um valor aleatório de 1 a 10

4. Qual o resultado esperado ?
R:O resultado esperado neste caso é que o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

5. Qual a sequência de passos a ser feitas para chegar ao resultado esperado ? 
R: 
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio
    print ('Chute foi maior que o valor gerado')
if chute < valor_aleatorio
    print ('Chute foi menor que o valor gerado')
if chute = valor_aleatorio
    print ('Você acertou!')

'''

import random

valor_aleatorio = random.randint(1,10)

acertou = False
while acertou == False:
    chute = int(input ('Chute um valor de 1 a 10'))
    if chute > valor_aleatorio:
        print('Chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('Chute foi menor que o valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou!')
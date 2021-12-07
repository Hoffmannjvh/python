#Fatorial de um número
'''
Crie um programa que recebe um número e imprime o seu fatorial.

# Método 5Q's para montar um algorítimo

Analise crticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais os dados de entradas necessários?
R: Número

2. O que devo fazer com estes dados?
R: Eu devo calcular o calcular o fatorial do número que for passado para o meu programa e o exibir na tela.

3. Quais são as restrições deste problema ?
R: O número deve ser um valor positivo e deve ser um valor inteiro

4. Qual o resultado esperado ?
R:O resultado esperado neste caso é que o fatorial do número providenciado seja exibido.

5. Qual a sequência de passos a ser feitas para chegar ao resultado esperado ? 
R: 
input numero
if numero > 0
if numero inteiro
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
print(fatorial)
'''

numero = int (input('Digite um número'))
if numero > 0:
    fatorial = 1
    for item in range (1,numero + 1):
        fatorial = fatorial * item
    print (fatorial)

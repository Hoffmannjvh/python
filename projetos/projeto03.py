#Medidor de velocidade
'''
Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ela tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "Não houve multa", caso esteja até 10km acima, deve exibir: "Levou multa grave", e caso esteja cima de 20 km da velocidade máxima, exiba: "Levou multa gravíssima".

1. Quais os dados de entradas necessários?
R: Velocidade

2. O que devo fazer com estes dados?
R: Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "Não houve multa", caso esteja até 10km acima, deve exibir: "Levou multa grave", e caso esteja cima de 20 km da velocidade máxima, exiba: "Levou multa gravíssima

3. 

4. Qual o resultado esperado ?
R: O resultado esperado é exibir a mensagem que corresponde ao nível da múlta que a pessoa levou (exibir: "Levou multa grave", e caso esteja cima de 20 km da velocidade máxima, exiba: "Levou multa gravíssima)

5. Qual a sequência de passos a ser feitas para chegar ao resultado esperado ? 
R: 
input velocidade
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print ('Não levou multa')
if velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10:
    print ('Você levou multa leve')
if velocidade > velocidade_maxima + 11 e velocidade <= velocidade_maxima + 20:
    print ('Levou multa grave')
if velocidade > velocidade_maxima + 20:
    print ('Levou multa gravíssima')
'''

velocidade = int(input('Digite sua velocidade '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave')
elif velocidade > velocidade_maxima + 20:
    print('Levou multa gravíssima')
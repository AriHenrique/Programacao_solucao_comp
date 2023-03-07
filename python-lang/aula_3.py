import math as mt


def verificar_float(variavel):
    variavel = variavel.replace(',', '.', 1)
    while True:
        if variavel.replace(".", "", 1).isdigit():
            return float(variavel)
        else:
            _loop = input("Infomer apenas números. Deseja Continuar?(Y/n): ").lower()
            if _loop[0] == "y" or _loop == "s":
                variavel = input("Informe novemente os dados: ").replace(',', '.', 1)
                continue
            else:
                print("\nNao foi possivel concluir o programa\n\nFim")
                quit()



print('1) Faça um programa que mostre a mensagem "Alo mundo" na tela.\n')

print("Hello World\n")

print('2) Faça um programa que peça um  número e então mostre a mensagem "O número informado foi [numero]\n')

number = verificar_float(input("Digite um número: "))
print(f'\nO número digitado foi {number}\n')

print('3) Faça um programa que peça dois números e imprima a soma.\n')

number_1 = verificar_float(input("Informe o primeiro número: "))
number_2 = verificar_float(input("Agora informe o segundo: "))

print(f'\nA soma dos dois números é {number_1 + number_2:.2f}\n')

print('4) Faça um programa que peça as 4 notas bimestrais e mostre a média\n')

nota_1 = verificar_float(input("Infomer a nota do seu primeiro semestre: "))
nota_2 = verificar_float(input("Infomer a nota do seu primeiro semestre: "))
nota_3 = verificar_float(input("Infomer a nota do seu primeiro semestre: "))
nota_4 = verificar_float(input("Infomer a nota do seu primeiro semestre: "))

print(f'\nA média dos 4 bimestres é {(nota_1 + nota_2 + nota_3 + nota_4) / 4:.2f}\n')

print('5) Faça um programa que converta metros para centímetros\n')

convert = verificar_float(input("Informe quantos metros deseja converter em cm: "))
print(f'\n{convert * 100:.2f} cm\n')

print('6) Faça um programa que peça o raio de um círculo, calcule e mostre sua área.\n')

raio = verificar_float(input("Informe o raio: "))
print(f'\nA área deste círculo é {mt.pi * raio ** 2:.2f}\n')

print('7) Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário\n')

area = verificar_float(input("Informe o valor de um dos lados do QUADRADO: "))
print(f'\nO dobro da área do quadrado é {area ** 2 * 2:.2f}\n')

print('8) Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e '
    'mostre o total do seu salário no referido mês.\n')

valor_horas = verificar_float(input("informe o valor da hora trabalhada: "))
horas_trabalhadas = verificar_float(input("\ninforme quantas horas foram trabalhadas: "))
print(f"\nTOTAL A RECEBER SERÁ R$ {valor_horas * horas_trabalhadas:.2f}\n")

print('9) Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus '
    'Celsius.\n')

temperatura_f = verificar_float(input("Digite a temperatura em Farenheit: "))
print(f'{temperatura_f:.1f}F equivale a {round((temperatura_f - 32) * (5 / 9)):.1f}C\n')

print("10) Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.\n")

temperatura_c = verificar_float(input("Digite a temperatura em Celsius: "))
print(f'{temperatura_c:.1f}C equivale a {round(temperatura_c * (9 / 5) + 32):.1f}F\n')

print('11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:\n'
    'a. o produto do dobro do primeiro com metade do segundo.\n'
    'b. a soma do tiplo do primeiro com o terceiro.\n'
    'c. o terceiro elevado ao cubo.\n')

num_int = int(verificar_float(input("Digite o primeiro numero inteiro: ")))
num_int_2 = int(verificar_float(input("Digite o segundo numero inteiro: ")))
num_float = verificar_float(input("Digite um valor real (Ex: 10.51): "))

print(f'\nA = {num_int * 2 * (num_int_2 / 2)}')
print(f'B = {3 * num_int + num_float}')
print(f'C = {num_float ** 3}\n')

print('12) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, '
    'usando a seguinte formula:\n(72.7*altura) - 58\n')

altura = verificar_float(input("Informe a sua altura em metros (Ex: 1.75m): "))
print(f'\nO peso ideal para a altura de {altura} é {72.7 * altura - 58:.1f}kg\n')

print("13) Tendo como dado de entrada a altura (m) de uma pessoa, construa um algoritmo que calcule seu peso ideal, "
    "utilizando as seguintes fórmulas:\n"
    "a. Para homens: (72.7*m) - 58\n"
    "b. Para mulheres: (62.1*m) - 44.7\n")

while True:
    tipo = input("Gostaria de calcular para homem ou mulher? ").lower()
    if tipo[0] == 'h':
        altura = verificar_float(input("Informe a altura em metros (Ex: 1.75m): "))
        print(f'\nO peso ideal para a altura de {altura} de um HOMEM é {72.7 * altura - 58:.1f}kg\n')
        break
    elif tipo[0] == 'm':
        altura = verificar_float(input("Informe a altura em metros (Ex: 1.75m): "))
        print(f'\nO peso ideal para a altura de {altura} de um HOMEM é {62.1 * altura - 44.7:.1f}kg\n')
        break
    else:
        loop = input('Tipo de sexo informado inválido. Deseja continuar?(Y/n): ').lower()
        if loop[0] == 'y':
            continue
        else:
            print("\nNao foi possivel concluir o programa\n\nFim")
            break


print("14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu \n"
    "trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do \n"
    "estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que vocè \n"
    "faça um programa quilos além do limite e na variavel multa o valor da multa que João devera pagar. Imprima os \n"
    "dados do programa com as mensagens adequadasS.")

total_pescaria = verificar_float(input("Qual o "))

# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o Sindicat0, taça um programa que nos de:
# a. salaro bruto.
# b. quanto pagou ao INSS.


alteracao

# C. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#
#     + Salário Bruto: RS
#     - IR IR (118) : R$
#     - INSS (88) R$
#     - Sindicato 58) : R$
#     = Salário Liquido: R$
#     Obs.: Salário Bruto - Descontos = Salário Liquido.
# 16. Faça um programa para uma loja de tintas. O programa devera pedir o tamanho em metros quadradoS da area a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# 17. Faça um Programa para uma loja de tintas. O programa deverà pedir o tamanho em metros quadrados da årea a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# o comprar apenas latas de 18 litros;
# o comprar apenas galðes de 3,6 litros;
# omisturar latas e galóes, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os
# valores para cima, isto é, considere latas cheias
# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
# Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

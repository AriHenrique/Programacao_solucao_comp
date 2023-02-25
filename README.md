# Aula de Programação e Soluções Computacionais (UNA-Aimorés)

## Aula dia 24/02

Calcule o salario bruto de acordo com o valor da hora e quantidade de horas trabalhadas
````py
print('Hello World')
print('Aula dia 24/02/2023')

while True:
    try:
        print("\nCALCULADORA DE SALARIO\n")

        valor_horas = float(input("informe o valor da hora trabalhada: "))
        horas_trabalhadas = float(input("\ninforme quantas horas foram trabalhadas: "))

        total_liquido = valor_horas * horas_trabalhadas

        print(f"TOTAL A RECEBER SERÁ {total_liquido:.2f}")
    except ValueError:
        loop = input("digite apenas números, deseja continuar?(Y/n)").lower()
        if loop[0] == 'y':
            continue
        else:
            print("FIM")
            break
````
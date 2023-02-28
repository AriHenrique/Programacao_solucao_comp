# 1

nome = input("Digite o seu nome: ")
dominio = input("\nAgora digite o domínio: ")

print(f"{nome}@{dominio}")

# 2
while True:
    try:
        valor_produto = float(input("Digite o valor do produto: "))

        total = valor_produto + ((valor_produto * 0.1) * 12)

        print(f"O valor total do produto será R${total:.2f}")
        break
    except ValueError:
        print("\nDigite apenas numeros\n")
        continue
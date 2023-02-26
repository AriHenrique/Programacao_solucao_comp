# Aula de Programação e Soluções Computacionais (UNA-Aimorés)

<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.15.1/devicon.min.css">
          
Guia de estudos das aulas do semestre 2023/01 da UNA — Aimorés. Todos os exercícios são obrigatórios na linguagem "Python", determinada pelo professor responsável, entretanto, resolvi fazer também na linguagem "Rust", uma vez que já havia aprendido a linguagem python, decidi refazer tudo usando uma outra linguagem que busco aprender e aprimorar, transformando os exercícios de python em rust. Toda a documentação das respectivas linguagens estão lincadas com a imagem, basta clique no ícone "<a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=20 align='top'/></a>" ou "<a href='https://devdocs.io/rust/'><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" align='top' width=25/></a>". 

Bons estudos!

# Aula dia 24/02

Calcule o salario bruto de acordo com o valor da hora e quantidade de horas trabalhadas

## Python <a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=26 align='center'/></a>

```py
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
```

## Rust <a href='https://devdocs.io/rust/'><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" align='center' width=35/></a>


```rs

fn main{
    
}

```

a
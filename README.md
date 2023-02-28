# Aula de Programação e Soluções Computacionais (UNA-Aimorés)

<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.15.1/devicon.min.css">

Guia de estudos das aulas do semestre 2023/01 UNA — Aimorés. Todos os exercícios são obrigatórios na linguagem "Python", determinada pelo professor responsável, entretanto, resolvi fazer também na linguagem "Rust", uma vez que já havia aprendido a linguagem python. Decidi refazer tudo usando uma outra linguagem que busco aprender e aprimorar, transformando os exercícios de python em rust. Toda a documentação das respectivas linguagens estão lincadas nos ícones.

## <a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=40 align='sub'/></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='https://devdocs.io/rust/'><img style="background-color: white" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width=40 align='text-top'/></a>

Bons estudos!

# Aula dia 24/02

Calcule o salario bruto de acordo com o valor da hora e quantidade de horas trabalhadas

## Python <a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=30 align='text-top'/></a>

```python
print('Hello World')
print('Aula dia 24/02/2023')

while True:
    try:
        print("\nCALCULADORA DE SALARIO\n")

        valor_horas = float(input("informe o valor da hora trabalhada: "))
        horas_trabalhadas = float(input("\ninforme quantas horas foram trabalhadas: "))

        total_liquido = valor_horas * horas_trabalhadas

        print(f"TOTAL A RECEBER SERÁ {total_liquido:.2f}")
        break
    except ValueError:
        loop = input("digite apenas números, deseja continuar?(Y/n)").lower()
        if loop[0] == 'y':
            continue
        else:
            print("FIM")
            break
```

## Rust <a href='https://devdocs.io/rust/'><img style="background-color: white" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width=30 align='text-top'/></a>


```rust
use std::io;

fn main() {
    println!("\nCALCULADORA DE SALARIO\n");

    let valor_horas: f64 = loop {
        println!("informe o valor da hora trabalhada: ");
        let input = get_input();
        match input.parse() {
            Ok(num) => break num,
            Err(_) => {
                println!("Digite apenas números.");
                continue;
            }
        }
    };

    let horas_trabalhadas: f64 = loop {
        println!("\ninforme quantas horas foram trabalhadas: ");
        let input = get_input();
        match input.parse() {
            Ok(num) => break num,
            Err(_) => {
                println!("Digite apenas números.");
                continue;
            }
        }
    };

    let total_liquido = valor_horas * horas_trabalhadas;

    println!("TOTAL A RECEBER SERÁ {:.2}", total_liquido);

    fn get_input() -> String {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Erro ao ler a entrada");
        input.trim().to_string()
    }
}
```

# Aula dia 27/02

## Python <a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=30 align='text-top'/></a>


```python
number1 = 30
number2 = 40

resultado = number1+number2

print(resultado)
```

1) Implemente um programa python que leia o nome de usuario e o dominio, produza a saida usuario@email

2) Implemente um programa python que solicite ao usuario o valor de um produto. Considere uma taxa de 0.1 ao mes exiba o valor total em um periodo de 12 meses.

```python
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
```

## Rust <a href='https://devdocs.io/rust/'><img style="background-color: white" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width=30 align='text-top'/></a>

```rust
fn main() {
    let number1 = 30;
    let number2 = 40;

    let result = number1+number2;

    println!("{}", result);
}
```

```rust
use std::io;

fn get_input() -> String {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Erro ao ler a entrada");
        input.trim().to_string()
}


fn exercice_1(){
    
    // exercice 1

    println!("Digite o seu nome: ");
    let mut nome = String::new();
    io::stdin().read_line(&mut nome).expect("Falha ao ler a entrada do usuário");
    nome = nome.trim().to_string();

    println!("Agora digite o dominio: ");
    let mut dominio = String::new();
    io::stdin().read_line(&mut dominio).expect("Falha ao ler a entrada do usuário");
    dominio = dominio.trim().to_string();
    println!("{}@{}", nome, dominio);
}


fn exercice_2(){

    // exercice 1

    let valor_produto: f32 = loop {
        println!("Digite o valor do produto: ");
        let valor_produto = get_input();
        break match valor_produto.parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Valor inválido! Digite apenas numeros");
                continue;
            }
        }    
    };

    let total = valor_produto + (valor_produto * 0.1 * 12.0);

    println!("O total é: {:.2}", total);
}


fn main() {
    exercice_1();
    exercice_2();
}
```

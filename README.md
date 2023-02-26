# Aula de Programação e Soluções Computacionais (UNA-Aimorés)

<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.15.1/devicon.min.css">
          
Guia de estudos das aulas do semestre 2023/01 da UNA — Aimorés. Todos os exercícios são obrigatórios na linguagem "Python", determinada pelo professor responsável, entretanto, resolvi fazer também na linguagem "Rust", uma vez que já havia aprendido a linguagem python, decidi refazer tudo usando uma outra linguagem que busco aprender e aprimorar, transformando os exercícios de python em rust. Toda a documentação das respectivas linguagens estão lincadas com a imagem, basta clique no ícone "<a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=20 align='sub'/></a>" ou "<a href='https://devdocs.io/rust/'><img style="background-color: white" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width=23 align='sub'/></a>". 


Bons estudos!

# Aula dia 24/02

Calcule o salario bruto de acordo com o valor da hora e quantidade de horas trabalhadas

## Python <a href="https://docs.python.org/3/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=30 align='text-top'/></a>

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

## Rust <a href='https://devdocs.io/rust/'><img style="background-color: white" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width=30 align='text-top'/></a>


```rs
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